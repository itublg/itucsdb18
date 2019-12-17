
from model.base import Base

class CustomerModel(Base):

    def __init__(self):
        super(CustomerModel, self).__init__()
        self.table_name = "CUSTOMERS"

    def create(self,*args,**kwargs):

        command = """ CREATE TABLE IF NOT EXISTS CUSTOMERS(
            customer_id serial PRIMARY KEY,
            customer_fullname varchar(50) NOT NULL,
            customer_address_id integer NOT NULL,
            customer_phone_number varchar(12) NOT NULL,
            customer_user_id integer NOT NULL,
            FOREIGN KEY (customer_address_id) REFERENCES ADDRESSES(address_id) ON UPDATE CASCADE,
            FOREIGN KEY (customer_user_id) REFERENCES USERS(user_id) ON UPDATE CASCADE
            );
        """
        self.execute(command)

    def insert(self,*args, **kwargs):
        command = """
        INSERT INTO CUSTOMERS(customer_fullname, customer_address_id,customer_phone_number,
        customer_user_id)
        VALUES ('{}','{}','{}','{}')
        """.format(*args)
        self.execute(command)
    def update(self,*args,**kwargs):

        raise NotImplementedError
    def delete(self,id):

        raise NotImplementedError
    def read(self,*args,**kwargs):
       raise NotImplementedError

customerModel = CustomerModel()

def createCustomer(customer_fullname,customer_address_id,customer_phone_number,customer_user_id):
    customerModel.insert(customer_fullname,customer_address_id,customer_phone_number,customer_user_id)
    return True
def getAllCustomer():
    command = """
    SELECT * FROM CUSTOMERS"""
    customer = customerModel.execute(command)
    return customer

def getCustomerById(id):
    command = """
    SELECT * FROM CUSTOMERS WHERE customer_id='{}'""".format(id)
    customer = customerModel.execute(command)
    return customer


def getCustomerByEmailAndPassword(email,password):
    command = """
    SELECT * FROM CUSTOMERS,USERS where email='{}'and password='{}' """.format(email, password)
    customer = customerModel.execute(command)
    return None if customer is None or len(customer) == 0 else customer[0]


def deleteCustomerById(id):
    command="""
    DELETE FROM CUSTOMERS WHERE customer_id = {}
    """.format(id)
    return customerModel.execute(command)


def updateCustomerById(id, customer_fullname, customer_address_id, customer_phone_number, customer_user_id):
    command = """  
    UPDATE CUSTOMERS SET customer_id='{}', customer_full_name='{}', customer_address_id='{}', customer_phone_number='{}', customer_user_id='{}'
    """.format(id, customer_fullname, customer_address_id, customer_phone_number, customer_user_id)

    return customerModel.execute(command)
def drop():
    command = """
        DELETE FROM CUSTOMERS"""
    return customerModel.execute(command)


def createCustomerTable():
    return customerModel.create()

def getCustomerByUserId(id):
    command = """
    SELECT * FROM CUSTOMERS WHERE customer_user_id ='{}' """.format(id)
    return customerModel.execute(command)