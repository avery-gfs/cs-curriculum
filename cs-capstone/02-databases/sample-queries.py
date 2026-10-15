import sqlite3

conn = sqlite3.connect("movies.db", autocommit=True)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

print("Top Movies:\n")

rows = conn.execute("""
SELECT * from movie
order by imdb_rank
limit 10
""")

for row in rows:
    print(dict(row))

print("\nOld Movies:\n")

rows = conn.execute("""
SELECT * from movie
order by year
limit 10
""")

for row in rows:
    print(dict(row))

print("\nNumber of Movies by Year:\n")

rows = conn.execute("""
SELECT year, count(*) as num_movies from movie
group by year
order by year
""")

for row in rows:
    print(dict(row))

print("\nTop Movie Years:\n")

rows = conn.execute("""
SELECT year, count(*) as num_movies, GROUP_CONCAT(title, ", ") as movies from movie
group by year
order by num_movies desc
limit 10
""")

for row in rows:
    print(dict(row))

print("\nFrequent Stars:\n")

rows = conn.execute("""
SELECT name, count(*) as num_roles from role
join person on person.id = role.person_id
group by person_id
order by num_roles desc
limit 20
""")

for row in rows:
    print(dict(row))

print("\nMovies per Genre:\n")

rows = conn.execute("""
SELECT genre.name, count(*) AS num_movies
from genre
join movie_genre on movie_genre.genre_id = genre.id
group by genre.id
order by num_movies desc;
""")

for row in rows:
    print(dict(row))

print("\nFrequent Directors:\n")

rows = conn.execute("""
SELECT person.name, count(*) AS films
from director
join person on person.id = director.person_id
group by person.id
having films >= 2
order by films desc;
""")

for row in rows:
    print(dict(row))

print("\nDecade Stats:\n")

rows = conn.execute("""
SELECT
    (year / 10) * 10 as decade, count(*) as num_movies,
    round(avg(runtime), 1) as avg_runtime,
    round(avg(imdb_rank), 1) as avg_rank
from movie
group by decade
order by decade;
""")

for row in rows:
    print(dict(row))

print("\nDivas:\n")

rows = conn.execute("""
SELECT DISTINCT person.name, movie.title, role_name
from director
join role on
    role.movie_id = director.movie_id
    and role.person_id = director.person_id
join person on person.id = director.person_id
join movie on movie.id = director.movie_id;
""")

for row in rows:
    print(dict(row))

print("\nDirector Actor Pairs:\n")

rows = conn.execute("""
SELECT d.name AS director, a.name AS actor, count(*) AS num_movies
from director
join role on role.movie_id = director.movie_id
join person d on d.id = director.person_id
join person a on a.id = role.person_id
where d.id != a.id
group by director.person_id, role.person_id
order by num_movies desc
limit 10;
""")

for row in rows:
    print(dict(row))
