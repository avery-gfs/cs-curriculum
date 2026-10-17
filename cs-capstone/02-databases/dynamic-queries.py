import sqlite3

conn = sqlite3.connect("movies.db", autocommit=True)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

search = "for"

print(f"Titles with '{search}':\n")

query = """
SELECT title, year from movie
where title like ?
"""

for row in conn.execute(query, [f"%{search}%"]):
    print(dict(row))

min_year = 1990
max_year = 2020
genre = "sci-fi"

print(f"\nGenre {genre} {min_year} - {max_year}:\n")

query = """
SELECT movie.title, movie.year from movie
join movie_genre on movie_genre.movie_id = movie.id
join genre on movie_genre.genre_id = genre.id
where year >= ? and year <= ? and genre.name = ? collate nocase
"""

rows = conn.execute(query, [min_year, max_year, genre])

for row in rows:
    print(dict(row))
