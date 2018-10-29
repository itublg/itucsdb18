from repository.user import UserRepository

user_repository = UserRepository()


def create_user(name, surname, username, password, email, bday):
    """
    params -> name, surname, username, password, email, birthday
    """
    user_repository.insert(name, surname, username, password, email, bday)
    user = user_repository.read(email, password)
    return user


def read_user(email, password):
    user = user_repository.read(email, password)
    return user


def get_user(email, password):
    """
    params -> email and password 
    used for fetching a one user for login operation
    """
    command = """
    SELECT * FROM users where email = '{}' and password = '{}' limit 1 
    """.format(email,password)
    user = user_repository.execute(command)
    return user[0]
    
