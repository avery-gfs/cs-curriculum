import sqlite3

conn = sqlite3.connect("movies.db", autocommit=True)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

rows = conn.execute("""
SELECT * from movie
order by imdb_rank
limit 10
""")

print("\nTop Movies:\n")

for row in rows:
    print(row["title"], row["imdb_rank"])

rows = conn.execute("""
SELECT * from movie
order by year
limit 10
""")

print("\nOld Movies:\n")

for row in rows:
    print(row["title"], row["year"])

rows = conn.execute("""
SELECT year, count(*) as movies from movie
group by year
order by year
""")

print("\nNumber of Movies by Year:\n")

for row in rows:
    print(row["year"], row["movies"])

rows = conn.execute("""
SELECT name, count(*) as roles from role
join person on person.id = role.person_id
group by person_id
order by roles desc
limit 20
""")

print("\nFrequent Stars:\n")

for row in rows:
    print(row["name"], row["roles"])

rows = conn.execute("""
SELECT genre.name, count(*) AS movies
FROM genre
JOIN movie_genre ON movie_genre.genre_id = genre.id
GROUP BY genre.id
ORDER BY movies DESC;
""")

print("\nMovies per Genre:\n")

for row in rows:
    print(row["name"], row["movies"])

rows = conn.execute("""
SELECT person.name, count(*) AS films
FROM director
JOIN person ON person.id = director.person_id
GROUP BY person.id
HAVING films >= 2
ORDER BY films DESC;
""")

print("\nFrequent Directors:\n")

for row in rows:
    print(row["name"], row["films"])

rows = conn.execute("""
SELECT
    (year / 10) * 10 AS decade, count(*) AS movies,
    round(avg(runtime), 1) AS avg_runtime,
    round(avg(imdb_rank), 1) AS avg_rank
FROM movie
GROUP BY decade
ORDER BY decade;
""")

print("\nDecade Stats:\n")

for row in rows:
    print(row["movies"], row["avg_runtime"], rows["avg_runtime"])
