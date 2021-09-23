import psycopg2
from app.services.config import configs
from psycopg2 import sql


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
        create_table()

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        keys = ["id", "anime", "released_date", "seasons"]
        columns = [sql.Identifier(key) for key in self.__dict__.keys()]
        values = [sql.Literal(value) for value in self.__dict__.values()]

        query = sql.SQL(
            """
                INSERT INTO
                    animes (id, {columns})
                VALUES
                    (DEFAULT, {values})
                RETURNING *;
            """
        ).format(
            columns=sql.SQL(',').join(columns),
            values=sql.SQL(',').join(values)
        )

        cur.execute(query)

        fetch_result = cur.fetchone()

        close_connection(conn, cur)

        for_dict = dict(zip(keys, fetch_result))

        return for_dict
