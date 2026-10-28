import json
import sqlite3
import sys

import ollama
import polars as pl

MODEL = "qwen2.5-coder:14b"
DB_PATH = "movies.db"
MAX_ATTEMPTS = 3

EXAMPLES = """
-- top 10 movies by imdb rank
SELECT * from movie order by imdb_rank limit 10

-- number of movies per year since 2000
SELECT year, count(*) as num_movies from movie where year >= 2000 group by year order by year

-- years with the most movies, and which movies they were
SELECT year, count(*) as num_movies, GROUP_CONCAT(title, ", ") as movies from movie group by year order by num_movies desc limit 10

-- stats per decade, including the top ranked movie of each decade
SELECT (year / 10) * 10 as decade, count(*) as num_movies, round(avg(runtime), 1) as avg_runtime, round(avg(imdb_rank), 1) as avg_rank, movie.title as top_movie, movie.year as top_movie_year, min(imdb_rank) as top_movie_rank from movie group by decade order by decade

-- actors with the most roles
SELECT name, count(*) as num_roles from role join person on person.id = role.person_id group by person_id order by num_roles desc limit 20

-- number of movies per genre
SELECT genre.name, count(*) AS num_movies from genre join movie_genre on movie_genre.genre_id = genre.id group by genre.id order by num_movies desc

-- 10 youngest actors (by age at time of movie)
SELECT person.name, person.birth_year, movie.year - person.birth_year as age, movie.title, movie.year from person join role on person.id = role.person_id join movie on movie.id = role.movie_id where person.birth_year is not null order by age limit 10

-- directors with at least 2 films
SELECT person.name, count(*) AS films from director join person on person.id = director.person_id group by person.id having films >= 2 order by films desc

-- directors who also acted in their own movies
SELECT person.name, movie.title, GROUP_CONCAT(role_name, ", ") as roles from director join role on role.movie_id = director.movie_id and role.person_id = director.person_id join person on person.id = director.person_id join movie on movie.id = director.movie_id group by person.name, movie.title

-- director / actor pairs who worked together on at least 4 movies
SELECT d.name AS director, a.name AS actor, count(*) AS num_movies from director join role on role.movie_id = director.movie_id join person d on d.id = director.person_id join person a on a.id = role.person_id where d.id != a.id group by director.person_id, role.person_id having num_movies >= 4 order by num_movies desc
"""

RESPONSE_FORMAT = {
    "type": "object",
    "properties": {"sql": {"type": "string"}},
    "required": ["sql"],
}


def open_db_readonly(path):
    # mode=ro makes sqlite refuse any write at the file level; query_only is a
    # second guard that rejects writes on this connection
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    conn.execute("PRAGMA query_only = ON")
    return conn


def get_schema(conn):
    rows = conn.execute(
        "SELECT sql from sqlite_master where type = 'table' and sql is not null"
    )
    return "\n".join(sql + ";" for (sql,) in rows)


def generate_sql(messages):
    response = ollama.chat(
        model=MODEL,
        messages=messages,
        format=RESPONSE_FORMAT,
        options={"temperature": 0},
    )
    return json.loads(response["message"]["content"])["sql"].strip()


def run_query(conn, sql):
    cursor = conn.execute(sql)
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    return pl.DataFrame(rows, schema=columns, orient="row", infer_schema_length=None)


def answer(conn, question):
    messages = [
        {
            "role": "system",
            "content": "You translate questions into a single read-only SQLite "
            "SELECT query against this schema:\n\n"
            + get_schema(conn)
            + "\n\nExample queries:\n"
            + EXAMPLES
            + '\nRespond with JSON of the form {"sql": "..."} containing '
            "only the query.",
        },
        {"role": "user", "content": question},
    ]

    for attempt in range(MAX_ATTEMPTS):
        sql = generate_sql(messages)
        print(sql, end="\n\n")
        try:
            return run_query(conn, sql)
        except sqlite3.Error as err:
            print(f"error: {err}\n")
            # give the model the error so it can fix its query
            messages.append({"role": "assistant", "content": json.dumps({"sql": sql})})
            messages.append({
                "role": "user",
                "content": f"That query failed with: {err}. Fix it.",
            })

    sys.exit(f"could not produce a working query after {MAX_ATTEMPTS} attempts")


def main():
    question = " ".join(sys.argv[1:]) or input("question: ")
    conn = open_db_readonly(DB_PATH)

    df = answer(conn, question)
    with pl.Config(
        tbl_rows=-1, tbl_cols=-1, fmt_str_lengths=80, tbl_hide_dataframe_shape=True
    ):
        print(df)


if __name__ == "__main__":
    main()
