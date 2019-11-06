import os
import sys
import psycopg2 as dbapi2



INIT_STATEMENTS = [
    "CREATE TABLE IF NOT EXISTS DUMMY (NUM INTEGER, FIRST_NAME VARCHAR(10))",
    "INSERT INTO DUMMY (NUM, FIRST_NAME) VALUES (45, 'HASAN')",
]

def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        sys.exit(1)
    initialize(url)
