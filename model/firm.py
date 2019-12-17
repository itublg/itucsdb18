
from model.base import Base

class FirmModel(Base):

    def __init__(self):
        super(FirmModel,self).__init__()
        self.table_name = "FIRMS"

    def create(self, *args, **kwargs):

        command = """ CREATE TABLE IF NOT EXISTS FIRMS(
            firm_id serial PRIMARY KEY,
            firm_name varchar(50) NOT NULL,
            firm_address_id integer NOT NULL,
            firm_user_id integer NOT NULL,
            firm_phone_number varchar(12) NOT NULL,
            FOREIGN KEY (firm_address_id) REFERENCES ADDRESSES(address_id) ON UPDATE CASCADE,          
            FOREIGN KEY (firm_user_id) REFERENCES USERS(user_id) ON UPDATE CASCADE
            )
        """
        self.execute(command)
    def insert(self,*args,**kwargs):
        command = """
        INSERT INTO FIRMS(firm_name, firm_address_id,
        firm_user_id,firm_phone_number)
        VALUES ('{}','{}','{}','{}')
        """.format(*args)
        self.execute(command)
    def update(self,*args,**kwargs):

        raise NotImplementedError
    def delete(self,id):

        raise NotImplementedError
    def read(self,*args,**kwargs):
       raise NotImplementedError

firmModel = FirmModel()

def createFirm(firm_name,firm_address_id,firm_user_id,firm_phone_number):

    firmModel.insert(firm_name, firm_address_id, firm_user_id, firm_phone_number)
    return True

def getAllFirm():
    command = """SELECT * FROM FIRMS"""
    firm = firmModel.execute(command)
    return firm
def deleteFirmById(id):
    command="""
    DELETE FROM FIRMS WHERE firm_id = {}
    """.format(id)
    return firmModel.execute(command)

def getFirmById(id):
    command = """
        SELECT * FROM FIRMS WHERE firm_id='{}'""".format(id)
    firm = firmModel.execute(command)
    return firm

def getFirmByEmailAndPassword(email,password):
    command = """
    SELECT * FROM FIRMS,USERS where email='{}'and password='{}' """.format(email,password)
    firm = firmModel.execute(command)
    return None if firm is None or len(firm) == 0 else firm[0]

def updateFirmById(id,firm_name ,firm_address_id ,firm_user_id ,firm_phone_number):
    command = """  
    UPDATE FIRMS SET firm_id='{}', firm_name='{}', firm_address_id='{}', firm_user_id='{}', firm_phone_number='{}'
    """.format(id, firm_name, firm_address_id, firm_user_id, firm_phone_number)

    return firmModel.execute(command)

def drop():
    command = """
        DELETE FROM FIRMS"""
    return firmModel.execute(command)

def createFirmTable():
    return firmModel.create()

def getFirmByUserId(id):

    command ="""SELECT * FROM FIRMS WHERE firm_user_id ='{}' """.format(id)
    return firmModel.execute(command)