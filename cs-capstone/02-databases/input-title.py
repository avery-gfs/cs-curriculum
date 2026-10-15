import sqlite3

conn = sqlite3.connect("movies.db", autocommit=True)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

query = input("Enter title query: ")
query = f"%{query}%"

rows = conn.execute(
    """
SELECT title from movie
where title like ?
""",
    [query],
)

for row in rows:
    print(dict(row))
