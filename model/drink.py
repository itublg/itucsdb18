
from model.base import Base

class DrinkModel(Base):

    def __init__(self):
        super(DrinkModel,self).__init__()
        self.table_name = "DRINKS"

    def create(self, *args, **kwargs):

        command = """ CREATE TABLE IF NOT EXISTS DRINKS(
            drink_id serial PRIMARY KEY,
            drink_name varchar(50) NOT NULL,
            supplier_id integer NOT NULL,
            drink_price decimal NOT NULL,
            FOREIGN KEY (supplier_id) REFERENCES FIRMS(firm_id) ON UPDATE CASCADE
            )
        """

        self.execute(command)
    def insert(self,*args,**kwargs):
        command = """
        INSERT INTO DRINKS (drink_name, supplier_id, drink_price)
        VALUES ('{}', '{}' , '{}' )
        """.format(*args)
        self.execute(command)

    def update(self, *args,  **kwargs):

        raise NotImplementedError
    def delete(self,id):

        raise NotImplementedError
    def read(self,*args,**kwargs):
       command="""SELECT * FROM DRINKS"""
       return self.execute(command)

drinkModel = DrinkModel()


def getAllDrink():
    command = """SELECT * FROM DRINKS"""
    return drinkModel.execute(command)


def getDrinkSupplierId(firmId):
    command = '''SELECT firm_name FROM DRINKS where supplier_id= {} '''.format(firmId)
    return drinkModel.execute(command)
def getDrinkListById(id):
    command = """SELECT * FROM DRINKS WHERE drink_id ='{}'""".format(id)
    return drinkModel.execute(command)
def deleteDrinkByName(name,id):
    command = """DELETE FROM DRINKS WHERE drink_name = '{}' and supplier_id = '{}'""".format(name, id)
    return drinkModel.execute(command)
def deleteDrink(id):
    command = """
       DELETE FROM DRINKS WHERE drink_id={} 
       """.format(id)
    return drinkModel.execute(command)

def createDrink(drink_name, supplier_id, drink_price):
    return drinkModel.insert(drink_name, supplier_id, drink_price)

def updateDrink(drink_name,supplier_id,drink_price,id):
    command ='''
        UPDATE DRINKS SET drink_name='{}', supplier_id='{}', drink_price='{}' where drink_id='{}'
    '''.format(drink_name,supplier_id, drink_price, id)
    return drinkModel.execute(command)
def drop():
    command = """
        DELETE FROM DRINKS"""
    return drinkModel.execute(command)

def createDrinkTable():
    return drinkModel.create()

def getDrinksBySupplierId(id):
    command = """SELECT * FROM DRINKS WHERE supplier_id = '{}' """.format(id)
    return drinkModel.execute(command)
def updateDrinkByName(price, name, id):
    command = """UPDATE DRINKS SET  drink_price='{}' WHERE drink_name='{}'and supplier_id = '{}'""".format(price,
                                                                                                            name,
                                                                                                            id)
    return drinkModel.execute(command)

def getDrinksByNameAndPrice(name, price):
    command = """SELECT * FROM DRINKS WHERE drink_name ='{}' and  drink_price= '{}'""".format(name,
                                                                                                    price)
    return drinkModel.execute(command)
