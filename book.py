import psycopg2 as dbapi2

class book:
	def __init__(self,
				name,
				pub_year,
				lang = None,
				genre = None,
				pub_location = None,
				publisher = None):
		self.name = name
		self.pub_year = pub_year
		self.lang = lang
		self.genre = genre
		self.pub_location = pub_location
		self.publisher = publisher

	def add_to_db(self,db_url):
		STATEMENT ='''
					INSERT INTO
					BOOKS	(NAME, PB_YR, LANG, GENRE, PB_LOC, PUBLISHER)
					VALUES 	('%s', '%s', '%s', '%s', '%s', '%s')
					ON CONFLICT(NAME,PB_YR) DO NOTHING
					''' % (self.name, self.pub_year, self.lang, self.genre, self.pub_location, self.publisher)

		with dbapi2.connect(db_url) as connection:
			cursor = connection.cursor()
			cursor.execute(STATEMENT)
			connection.commit()
