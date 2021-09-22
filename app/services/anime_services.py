import psycopg2
from psycopg2 import sql
from app.services.config import configs


def close_connection(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


def create_table():

    conn = psycopg2.connect(**configs)
    cur = conn.cursor()

    query = sql.SQL(
        """
            CREATE TABLE IF NOT EXISTS animes(
                id BIGSERIAL PRIMARY KEY,
                anime VARCHAR(100) NOT NULL UNIQUE,
                released_date DATE NOT NULL,
                seasons INTEGER NOT NULL
            )
        """
    )
    cur.execute(query)
    close_connection(conn, cur)


class Animes():
    def __init__(self, anime: str, released_date, seasons: int) -> None:
        self.anime = anime.title()
        self.released_date = released_date
        self.seasons = seasons

    def save(self):
        ...
