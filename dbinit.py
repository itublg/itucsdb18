
import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
     "CREATE TABLE IF NOT EXISTS TEST(address_id serial PRIMARY KEY) ",
    "INSERT INTO TEST  VALUES (43)",

]
showDB = "SELECT * FROM TEST"



#url = "postgres://postgres:docker@localhost:5432/postgres"



def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        
        cursor.execute(INIT_STATEMENTS[0])

        cursor.close()


if __name__ == "__main__":

    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file= sys.stderr)
        sys.exit(1)
    initialize(url)
   





