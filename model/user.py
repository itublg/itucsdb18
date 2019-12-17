from model.base import Base


class UserModel(Base):

    def __init__(self):

        super(UserModel, self).__init__()
        self.table_name = "USERS"
        # self.create()

    def create(self, *args, **kwargs):
        """
        Create table users
        """
        command = """
        CREATE TABLE USERS (
            user_id serial PRIMARY KEY,
            username varchar(30) UNIQUE ,
            password varchar(16) NOT NULL,
            usertype integer NOT NULL,
            email varchar(30) UNIQUE NOT NULL
        )
        """
        self.execute(command)

    def insert(self, *args, **kwargs):

        command = """
        INSERT INTO USERS 
         (username, password, email, usertype)
            VALUES ('{}', '{}', '{}', '{}' )  
        """.format(*args)
        self.execute(command)

    def update(self, *args, **kwargs):

        raise NotImplementedError

    def delete(self, *args, **kwargs):

        raise NotImplementedError

    def read(self, *args, **kwargs):

        raise NotImplementedError


userModel = UserModel()


def create_user(username, password, email, usertype):

    userModel.insert(username, password, email, usertype)
    user = get_user(email, password)
    return user

def getUserId(username, password, email, usertype):
    command = """
            SELECT user_id FROM USERS WHERE username = '{}' AND password ='{}' AND email='{}' AND usertype ='{}'
            """.format(username, password, email, usertype)
    return userModel.execute(command)
def get_user(email, password):
    command = """
    SELECT * FROM USERS WHERE email = '{}' and password = '{}'
    """.format(email, password)
    user = userModel.execute(command)
    print("model:", user)
    return None if user is None or len(user) == 0 else user[0]


def createUserTable():
    return userModel.create()