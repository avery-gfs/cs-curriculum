import requests, json

task = "the 10 oldest actors (by age at time of movie). include name, age, movie name, movie year"

sch = """
CREATE TABLE movie(
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  year INTEGER,
  runtime INTEGER,
  imdb_rank INTEGER
);
CREATE TABLE genre(id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE);
CREATE TABLE movie_genre(
  movie_id INTEGER NOT NULL REFERENCES movie(id),
  genre_id INTEGER NOT NULL REFERENCES genre(id),
  PRIMARY KEY(movie_id, genre_id)
);
CREATE TABLE person(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  birth_year INTEGER
);
CREATE TABLE director(
  movie_id INTEGER NOT NULL REFERENCES movie(id),
  person_id INTEGER NOT NULL REFERENCES person(id),
  PRIMARY KEY(movie_id, person_id)
);
CREATE TABLE role(
  id INTEGER PRIMARY KEY,
  movie_id INTEGER NOT NULL REFERENCES movie(id),
  person_id INTEGER NOT NULL REFERENCES person(id),
  role_name TEXT
);
"""

schema = {
    "type": "object",
    "properties": {"sql": {"type": "string"}},
    "required": ["sql"],
}

r = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "qwen2.5-coder:7b",
        "stream": False,
        "format": schema,
        "options": {"temperature": 0},
        "messages": [
            {
                "role": "system",
                "content": "Translate the user's request into one SQLite query for this schema:\n"
                + sch
                + "Respond with JSON containing only the SQL.",
            },
            {"role": "user", "content": task},
        ],
    },
)
sql = json.loads(r.json()["message"]["content"])["sql"]
print(sql)
