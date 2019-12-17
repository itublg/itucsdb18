
from model.base import Base

class OrderModel(Base):

    def __init__(self):
        super(OrderModel,self).__init__()
        self.table_name = "ORDERS"

    def create(self, *args, **kwargs):

        command = """ CREATE TABLE IF NOT EXISTS ORDERS(
            order_id serial PRIMARY KEY,
            product_id integer DEFAULT NULL,
            dessert_id integer DEFAULT NULL,
            drink_id integer DEFAULT NULL,
            customer_order_id integer NOT NULL,
            
            FOREIGN KEY (customer_order_id) REFERENCES CUSTOMERS(customer_id) ON UPDATE CASCADE,
            FOREIGN KEY (dessert_id) REFERENCES DESSERTS(dessert_id) ON UPDATE CASCADE,
            FOREIGN KEY (drink_id) REFERENCES DRINKS(drink_id) ON UPDATE CASCADE,
            FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id) ON UPDATE CASCADE
            )
        """
        self.execute(command)
    def insert(self,*args,**kwargs):
        command = """
        INSERT INTO ORDERS(product_id, dessert_id, drink_id, customer_order_id)
        VALUES ('{}','{}', '{}','{}')
        """.format(*args)
        self.execute(command)

    def update(self,*args,**kwargs):

        raise NotImplementedError
    def delete(self,id):

        raise NotImplementedError
    def read(self,*args,**kwargs):
       command="""SELECT * FROM ORDERS"""
       return self.execute(command)

orderModel = OrderModel()

def createOrder(product_id,dessert_id,drink_id,customer_order_id):

    if product_id == None and drink_id != None and dessert_id == None :
        command = """
            INSERT INTO ORDERS(drink_id, customer_order_id)
            VALUES ('{}','{}')
            """.format( drink_id, customer_order_id)
        return orderModel.execute(command)
    if product_id == None and drink_id == None and dessert_id != None :
        command = """
            INSERT INTO ORDERS(dessert_id, customer_order_id)
            VALUES ('{}','{}')
            """.format( dessert_id, customer_order_id)
        return orderModel.execute(command)

    if product_id == None and drink_id != None and dessert_id != None :
        command = """
            INSERT INTO ORDERS(dessert_id, drink_id, customer_order_id)
            VALUES ('{}','{}','{}')
            """.format( dessert_id, drink_id, customer_order_id)
        return orderModel.execute(command)

    if product_id != None and drink_id == None and dessert_id == None:
        command = """
                   INSERT INTO ORDERS(product_id, customer_order_id)
                   VALUES ('{}','{}')
                   """.format(product_id, customer_order_id)
        return orderModel.execute(command)
    if product_id != None and drink_id != None and dessert_id == None:
        command = """
                  INSERT INTO ORDERS(product_id,drink_id, customer_order_id)
                  VALUES ('{}','{}','{}')
                  """.format(product_id, drink_id, customer_order_id)
        return orderModel.execute(command)
    if product_id != None and dessert_id != None and drink_id == None :
        command = """
               INSERT INTO ORDERS(product_id,dessert_id, customer_order_id)
               VALUES ('{}','{}','{}')
               """.format(product_id, dessert_id, customer_order_id)
        return orderModel.execute(command)

    if product_id != None and drink_id != None and dessert_id != None :
        command = """
            INSERT INTO ORDERS(product_id,dessert_id, drink_id, customer_order_id)
            VALUES ('{}','{}','{}','{}')
            """.format(product_id, dessert_id, drink_id, customer_order_id)
        return orderModel.execute(command)
def getAllOrder():
    command = """
    SELECT * FROM ORDERS"""
    order = orderModel.execute(command)
    return order
def getOrderListById(id):
    command = """SELECT * FROM ORDERS where order_id = {} """.format(id)
    return orderModel.execute(command)

def deleteOrderById(id):
    command = """
       DELETE FROM ORDERS WHERE order_id= {} 
       """.format(id)
    return orderModel.execute(command)

def updateOrder(product_id, desert_id, drink_id,customer_order_id):
    command ="""
    UPDATE ORDERS SET product_id='{}' AND dessert_id = '{}' AND drink_id ='{}'AND customer_order_id='{}' 
    """.format(id,product_id, desert_id, drink_id, customer_order_id)
    return orderModel.execute(command)

def drop():
    command = """
        DELETE FROM ORDERS"""
    return orderModel.execute(command)

def createOrderTable():
    return orderModel.create()


def getOrdersByCustomerId(id):
    command = """SELECT * FROM ORDERS WHERE customer_order_id ='{}'""".format(id)
    return orderModel.execute(command)
def getProductIds(id):
    command = """SELECT product_id FROM ORDERS WHERE customer_order_id ='{}'""".format(id)
    return orderModel.execute(command)

def getDessertIds(id):
    command = """SELECT dessert_id FROM ORDERS WHERE customer_order_id ='{}'""".format(id)
    return orderModel.execute(command)
def getDrinkIds(id):
    command = """SELECT drink_id FROM ORDERS WHERE customer_order_id ='{}'""".format(id)
    return orderModel.execute(command)

def deleteOrder(customer_order_id):
    command = """
                DELETE FROM ORDERS WHERE customer_order_id='{}'
                """.format( customer_order_id)
    return orderModel.execute(command)

def deleteDessertOrder(dessert_id, customer_order_id):
    command = """
                   DELETE FROM ORDERS WHERE dessert_id ='{}' AND customer_order_id='{}'
                   """.format(dessert_id, customer_order_id)
    return orderModel.execute(command)

def deleteDrinkOrder(drink_id, customer_order_id):
    command = """
                   DELETE FROM ORDERS WHERE drink_id ='{}' AND customer_order_id='{}'
                   """.format(drink_id, customer_order_id)
    return orderModel.execute(command)