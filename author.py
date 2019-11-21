
import psycopg2 as dbapi2

class author:
	def __init__(self,
				name,
				last_name,
				birth_year = None,
				birth_place = None,
				last_book_date = None,
				last_book_name = None,
				):
		self.name = name
		self.last_name = last_name
		self.birth_year = birth_year
		self.birth_place = birth_place
		self.last_book_date = last_book_date
		self.last_book_name = last_book_name

	def add_to_db(self,db_url):
		STATEMENT ='''
					INSERT INTO
					AUTHORS	(NAME, PB_YR, LANG, GENRE, PB_LOC, PUBLISHER)
					VALUES 	('%s', '%s', '%s', '%s', '%s', '%s')
					ON CONFLICT(NAME,PB_YR) DO NOTHING
					''' % (self.name, self.birth_year, self.birth_place, self.last_book_date, self.last_book_name)

		with dbapi2.connect(db_url) as connection:
			cursor = connection.cursor()
			cursor.execute(STATEMENT)
			connection.commit()
