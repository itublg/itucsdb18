
from model.base import Base

class ProductModel(Base):

    def __init__(self):
        super(ProductModel,self).__init__()
        self.table_name = "PRODUCTS"

    def create(self, *args, **kwargs):

        command = """ CREATE TABLE IF NOT EXISTS PRODUCTS(
            product_id serial PRIMARY KEY,
            product_name varchar(50) NOT NULL,
            supplier_id integer NOT NULL,
            product_price decimal NOT NULL,
            FOREIGN KEY (supplier_id) REFERENCES FIRMS(firm_id) ON UPDATE CASCADE
            )
        """

        self.execute(command)
    def insert(self,*args,**kwargs):
        command = """
        INSERT INTO PRODUCTS (product_name,supplier_id,product_price)
        VALUES ('{}', '{}' , '{}' )
        """.format(*args)
        self.execute(command)

    def update(self, *args,  **kwargs):

        raise NotImplementedError
    def delete(self,id):

        raise NotImplementedError
    def read(self,*args,**kwargs):
       command="""SELECT * FROM PRODUCTS"""
       return self.execute(command)

productModel = ProductModel()


def getAllProduct():
    command = """SELECT * FROM PRODUCTS"""
    return productModel.execute(command)


def getProductSupplierId(firmId):
    command = '''SELECT firm_name FROM PRODUCTS where supplier_id= {} '''.format(firmId)
    return productModel.execute(command)
def getProductListById(id):
    command = """SELECT * FROM PRODUCTS WHERE product_id ='{}'""".format(id)
    return productModel.execute(command)
def deleteProductByName(name,id):
    command = """DELETE FROM PRODUCTS WHERE product_name = '{}' and supplier_id = '{}'""".format(name, id)
    return productModel.execute(command)
def deleteProduct(id):
    command = """
       DELETE FROM PRODUCTS WHERE product_id={} 
       """.format(id)
    return productModel.execute(command)

def createProduct(product_name,supplier_id,product_price):
    return productModel.insert(product_name,supplier_id,product_price)

def updateProduct(product_name,supplier_id,product_price,id):
    command ='''
        UPDATE PRODUCTS SET product_name='{}', supplier_id='{}', product_price='{}' where product_id='{}'
    '''.format(product_name,supplier_id,product_price,id)
    return productModel.execute(command)
def drop():
    command = """
        DELETE FROM PRODUCTS"""
    return productModel.execute(command)

def createProductTable():
    return productModel.create()

def getProductsBySupplierId(id):
    command = """SELECT * FROM PRODUCTS WHERE supplier_id = '{}' """.format(id)
    return productModel.execute(command)
def updateProductByName(price, name, id):
    command = """UPDATE PRODUCTS SET  product_price='{}' WHERE product_name='{}'and supplier_id = '{}'""".format(price, name, id)
    return productModel.execute(command)

def getProductsByNameAndPrice(name, price):
    command = """SELECT * FROM PRODUCTS WHERE product_name ='{}' and  product_price= '{}'""".format(name, price)
    return productModel.execute(command)
