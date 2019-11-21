import psycopg2 as dbapi2

class student:
	def __init__(self,
				name,
				last_name,
				faculty,
				department,
				grade,
				membership_start_date,
				debt = 0):
		self.name = name
		self.last_name = last_name
		self.faculty = faculty
		self.department = department
		self.grade = grade
		self.membership_start_date = membership_start_date
		self.debt = debt

	def add_to_db(self,db_url):
		STATEMENT ='''
					INSERT INTO 
					STUDENTS (NAME, LAST_NAME, FACULTY, DEPART, GRADE, MEM_DATE, DEBT) 
					VALUES 	('%s', '%s', '%s', '%s', '%d', '%s', '%f') 
					''' % (self.name, self.last_name, self.faculty, self.department, self.grade, self.membership_start_date, self.debt)
				
		with dbapi2.connect(db_url) as connection:
			cursor = connection.cursor()
			cursor.execute(STATEMENT)
			cursor.close()

