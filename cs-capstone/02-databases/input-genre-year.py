import sqlite3

conn = sqlite3.connect("movies.db", autocommit=True)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

min_year = input("Enter minimum year: ")
max_year = input("Enter maximum year: ")
genre = input("Enter genre: ")

rows = conn.execute(
    """
SELECT movie.title, movie.year from movie
join movie_genre on movie_genre.movie_id = movie.id
join genre on movie_genre.genre_id = genre.id
where year >= ? and year <= ? and genre.name like ?
""",
    [min_year, max_year, genre],
)

for row in rows:
    print(dict(row))
