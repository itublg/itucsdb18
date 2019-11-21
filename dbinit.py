import os
import sys

import psycopg2 as dbapi2

def init_book_table(url):
	statement = '''
		CREATE TABLE BOOKS(
			ID SERIAL,
			NAME VARCHAR(80) NOT NULL,
			PB_YR CHAR(4) NOT NULL,
			PB_LOC VARCHAR(80),
			PUBLISHER VARCHAR(80),
			GENRE VARCHAR(20),
			LANG VARCHAR(20),
			

			UNIQUE(NAME,PB_YR),
			PRIMARY KEY(ID)

		)'''
	with dbapi2.connect(url) as connection:
		cursor = connection.cursor()
		cursor.execute("DROP TABLE IF EXISTS BOOKS")
		connection.commit()

	with dbapi2.connect(url) as connection:
		cursor = connection.cursor()
		cursor.execute(statement)
		connection.commit()


def init_author_table(url):

	statement = '''
		CREATE TABLE AUTHORS(
			ID SERIAL,
			NAME VARCHAR(40) NOT NULL,
			LAST_NAME VARCHAR(40) NOT NULL,
			BIRTH_YR CHAR(4),
			BIRTH_PLACE VARCHAR(40),
			LAST_BOOK_DATE VARCHAR(40),
			LAST_BOOK_NAME VARCHAR(40),

			PRIMARY KEY(ID)
		)'''

	with dbapi2.connect(url) as connection:
		cursor = connection.cursor()
		cursor.execute("DROP TABLE IF EXISTS AUTHORS")
		connection.commit()
	with dbapi2.connect(url) as connection:
		cursor = connection.cursor()
		cursor.execute(statement)
		connection.commit()


def init_student_table(url):

	statement = '''
		CREATE TABLE STUDENTS(
			ID SERIAL,
			NAME VARCHAR(40) NOT NULL,
			LAST_NAME VARCHAR(40) NOT NULL,
			FACULTY VARCHAR(40) NOT NULL,
			DEPART VARCHAR(40) NOT NULL,
			GRADE INTEGER NOT NULL,
			MEM_DATE VARCHAR(40),
			DEBT FLOAT,

			PRIMARY KEY(ID)
		)'''
	with dbapi2.connect(url) as connection:
		cursor = connection.cursor()
		cursor.execute("DROP TABLE IF EXISTS STUDENTS")
		connection.commit()
	with dbapi2.connect(url) as connection:
		cursor = connection.cursor()
		cursor.execute(statement)
		connection.commit()
