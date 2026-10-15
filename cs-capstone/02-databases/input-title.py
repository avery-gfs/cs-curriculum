import sqlite3

conn = sqlite3.connect("movies.db", autocommit=True)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

title = input("Enter title: ")

query = """
SELECT title from movie
where title like ?
"""

for row in conn.execute(
    query,
    [f"%{title}%"],
):
    print(dict(row))
