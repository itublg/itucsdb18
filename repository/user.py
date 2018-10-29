from repository.base import Base


class UserRepository(Base):

    def __init__(self):
        super(UserRepository, self).__init__()
        self.create()

    def create(self, *args, **kwargs):
        command = """
        CREATE TABLE users (
            id serial PRIMARY KEY,
            name varchar(30) NOT NULL,
            surname varchar(30) NOT NULL,
            username varchar(30) UNIQUE NOT NULL,
            password varchar(16) NOT NULL,
            email varchar(30) UNIQUE NOT NULL,
            birthday date NOT NULL,
            createdate timestamp NOT NULL,
            updatedate timestamp NULL,
            deleted bool NULL
        )
        """
        self.execute(command)

    def insert(self, *args, **kwargs):
        """ 
        params -> name, surname, username, password, email, birthday
        """
        command = """
        INSERT INTO users (
            name, surname, username, password, email, birthday, createdate)
            values ('{}', '{}', '{}', '{}', '{}', '{}', now() )  
        """.format(*args, )
        self.execute(command)

    def update(self, *args, **kwargs):
        command = """
        UPDATE users {} SET {} WHERE {}
        """
        self.execute(command)

    def delete(self, *args, **kwargs):
        command = """
        DELETE {} WHERE {} 
        """
        self.execute(command)

    def read(self, *args, limit = 1, **kwargs):
        command = """
        SELECT {} FROM USERS WHERE {} AND deleted is null
        """.format()
        return self.execute(command)
