
from model.base import Base

class DessertModel(Base):

    def __init__(self):
        super(DessertModel,self).__init__()
        self.table_name = "DESSERTS"

    def create(self, *args, **kwargs):

        command = """ CREATE TABLE IF NOT EXISTS DESSERTS(
            dessert_id serial PRIMARY KEY,
            dessert_name varchar(50) NOT NULL,
            supplier_id integer NOT NULL,
            dessert_price decimal NOT NULL,
            FOREIGN KEY (supplier_id) REFERENCES FIRMS(firm_id) ON UPDATE CASCADE
            )
        """

        self.execute(command)
    def insert(self,*args,**kwargs):
        command = """
        INSERT INTO DESSERTS (dessert_name,supplier_id,dessert_price)
        VALUES ('{}', '{}' , '{}' )
        """.format(*args)
        self.execute(command)

    def update(self, *args,  **kwargs):

        raise NotImplementedError
    def delete(self,id):

        raise NotImplementedError
    def read(self,*args,**kwargs):
       command="""SELECT * FROM DESSERTS"""
       return self.execute(command)

dessertModel = DessertModel()


def getAllDessert():
    command = """SELECT * FROM DESSERTS"""
    return dessertModel.execute(command)


def getDessertSupplierId(firmId):
    command = '''SELECT firm_name FROM DESSERTS where supplier_id= {} '''.format(firmId)
    return dessertModel.execute(command)
def getDessertListById(id):
    command = """SELECT * FROM DESSERTS WHERE dessert_id ='{}'""".format(id)
    return dessertModel.execute(command)
def deleteDessertByName(name,id):
    command = """DELETE FROM DESSERTS WHERE dessert_name = '{}' and supplier_id = '{}'""".format(name, id)
    return dessertModel.execute(command)
def deleteDessert(id):
    command = """
       DELETE FROM DESSERTS WHERE dessert_id={} 
       """.format(id)
    return dessertModel.execute(command)

def createDessert(dessert_name,supplier_id,dessert_price):
    return dessertModel.insert(dessert_name,supplier_id, dessert_price)

def updateDessert(dessert_name,supplier_id,dessert_price,id):
    command ='''
        UPDATE DESSERTS SET dessert_name='{}', supplier_id='{}', dessert_price='{}' where dessert_id='{}'
    '''.format(dessert_name, supplier_id, dessert_price, id)
    return dessertModel.execute(command)
def drop():
    command = """
        DELETE FROM DESSERTS"""
    return dessertModel.execute(command)

def createDessertTable():
    return dessertModel.create()

def getDessertsBySupplierId(id):
    command = """SELECT * FROM DESSERTS WHERE supplier_id = '{}' """.format(id)
    return dessertModel.execute(command)
def updateDessertByName(price, name, id):
    command = """UPDATE DESSERTS SET  dessert_price='{}' WHERE dessert_name='{}'and supplier_id = '{}'""".format(price,
                                                                                                                 name,
                                                                                                                 id)
    return dessertModel.execute(command)

def getDessertsByNameAndPrice(name, price):
    command = """SELECT * FROM DESSERTS WHERE dessert_name ='{}' and  dessert_price= '{}'""".format(name,
                                                                                                    price)
    return dessertModel.execute(command)
