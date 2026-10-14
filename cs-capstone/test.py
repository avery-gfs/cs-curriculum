import sqlite3

conn = sqlite3.connect("movies.db", autocommit=True)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

for row in conn.execute("SELECT * FROM movie WHERE imdb_rank = 1"):
    print(row)
