CREATE TABLE movie (
  id             INTEGER PRIMARY KEY,
  title          TEXT NOT NULL,
  year           INTEGER,
  runtime        INTEGER,        -- minutes
  content_rating TEXT,           -- e.g. 'PG-13'
  imdb_rank      INTEGER         -- Top 250 position
);

CREATE TABLE genre (
  id   INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE movie_genre (
  movie_id INTEGER NOT NULL REFERENCES movie(id),
  genre_id INTEGER NOT NULL REFERENCES genre(id),
  PRIMARY KEY (movie_id, genre_id)
);

CREATE TABLE person (
  id         INTEGER PRIMARY KEY,
  name       TEXT NOT NULL,
  birth_date TEXT                -- 'YYYY-MM-DD'
);

CREATE TABLE director (
  movie_id  INTEGER NOT NULL REFERENCES movie(id),
  person_id INTEGER NOT NULL REFERENCES person(id),
  PRIMARY KEY (movie_id, person_id)
);

CREATE TABLE role (
  id        INTEGER PRIMARY KEY,
  movie_id  INTEGER NOT NULL REFERENCES movie(id),
  person_id INTEGER NOT NULL REFERENCES person(id),
  role_name TEXT
);
