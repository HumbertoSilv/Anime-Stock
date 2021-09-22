import psycopg2
from psycopg2 import sql
from app.services.config import configs


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

    conn.commit()
    cur.close()
    conn.close()


class Animes():
    ...
