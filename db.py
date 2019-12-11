import psycopg2 as dbapi2
import os
import sys
import threading

dataBaseLock = threading.Lock()

val = 1

LOCAL = False

# def connectDb():
#     url = os.getenv("DATABASE_URL")
#     if url is None:
#        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
#        sys.exit(1)

#     return initialize(url)


_connection = None

def get_connection():
    if LOCAL:
        url = "dbname='testpython' user='matt' host='localhost' " + \
                  "password='test1234'"
    else:
        url = os.getenv("DATABASE_URL")

    global _connection
    if not _connection:
        _connection = dbapi2.connect(url)
    return _connection

def get_cursor():
    return get_connection().cursor()