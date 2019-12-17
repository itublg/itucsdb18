
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint

from endpoints.utils import login_required, view, login_required_action

from model.order import *
from model.drink import *
from model.dessert import *
from model.product import *
from model.customer import *

order = Blueprint('order' ,__name__, url_prefix='/order')

@login_required
@order.route("/", methods=["GET"])
@view
def getAllOrderEnd(*args, **kwargs):
    if session["logged_in"][3] == 1:
        orderAll = getAllOrder()
        if orderAll is None:
            orderAll = []
        return render_template("order/firmorders.html", orders=orderAll, **kwargs)

    else:
        id = session["logged_in"][0]
        customer = getCustomerByUserId(id)
        print(customer[0][0])


        products = []
        desserts = []
        drinks = []
        if customer is None:
            customer = []
        else:
            if getOrdersByCustomerId(customer[0][0]) is None:
                products = []
                desserts = []
                drinks  = []
            else:
                print(getOrdersByCustomerId(customer[0][0]))
                for i in getOrdersByCustomerId(customer[0][0]):
                        print ("i->:",i)
                        if i[1] is not None:
                            products.append(getProductListById(i[1])[0])
                        if i[2] is not None:
                            desserts.append(getDessertListById(i[2])[0])
                        if i[3] is not None:
                            drinks.append(getDrinkListById(i[3])[0])

                print(products)
                print(desserts)
                print(drinks)

        if products is None:
            products = []
            desserts = []
            drinks   = []
        return render_template("order/customerorders.html", orders=products, desserts=desserts, drinks=drinks, **kwargs)




@order.route("/create", methods = ["GET" ,"POST"])
@login_required
@view
def createOrderEnd(*args, **kwargs):
    if request.method == "GET":
        return render_template(("order/createOrder.html", *kwargs))
    if request.form["productname"]is not None and request.form["price"]:
        product_name = request.form["productname"]
        product_price = request.form["price"]
    else:
        product_name = None
        product_price = None

    if request.form["dessertname"] is not None and request.form["pricedessert"] is not None:
        dessert_name = request.form["dessertname"]
        dessert_price = request.form["pricedessert"]
    else:
        dessert_name = None
        dessert_price = None
    if request.form["drinkname"] is not None and request.form["pricedrink"] is not None:
        drink_name = request.form["drinkname"]
        drink_price = request.form["pricedrink"]
    else:
        drink_name = None
        drink_price = None

    print("pn",product_name,"pp",product_price,"dn",dessert_name,"dp",dessert_price,"drn",drink_name,"drp",drink_price)

    customer_order_id = getCustomerByUserId(session["logged_in"][0])
    if product_name is None or product_price is None:
        product_id = []
    else:
        product_id = getProductsByNameAndPrice(product_name, product_price)
    if dessert_name is None or dessert_price is None:
        dessert_id = []
    else:
        dessert_id = getDessertsByNameAndPrice(dessert_name, dessert_price)
    if drink_name is None or drink_price is None:
        drink_id = []
    else:
        drink_id = getDrinksByNameAndPrice(drink_name, drink_price)


    if customer_order_id is None:
        customer_order_id = []
    if product_id is None:
        product_id = []
        print("Non product")
    if dessert_id is None:
            dessert_id = []
            print("Non dessert")
    if drink_id is None:
        drink_id = []
        print("Non drink")

    if len(product_id) !=0 and len(dessert_id) !=0 and len(drink_id) !=0:
        createOrder(product_id[0][0], dessert_id[0][0], drink_id[0][0], customer_order_id[0][0])
    if len(product_id) != 0 and len(dessert_id) != 0 and len(drink_id) == 0:
        createOrder(product_id[0][0], dessert_id[0][0], None, customer_order_id[0][0])
    if len(product_id) !=0 and len(dessert_id) == 0 and len(drink_id) != 0:
        createOrder(product_id[0][0], None, drink_id[0][0], customer_order_id[0][0])
    if len(product_id) == 0 and len(dessert_id) !=0 and len(drink_id) != 0 :
        createOrder(None, dessert_id[0][0], drink_id[0][0], customer_order_id[0][0])
    if len(product_id) ==0 and len(dessert_id) == 0 and len(drink_id) != 0:
        createOrder(None, None, drink_id[0][0], customer_order_id[0][0])
    if len(product_id) == 0 and len(dessert_id) != 0 and len(drink_id) == 0:
        createOrder(None, dessert_id[0][0], None, customer_order_id[0][0])
    if len(product_id) != 0 and len(dessert_id)  ==0 and len(drink_id) == 0:
        createOrder(product_id[0][0], None, None, customer_order_id[0][0])


    if len(product_id)== 0 and len( dessert_id) == 0 and len(drink_id) == 0:
        print("All query are false")
        return redirect(url_for("order.getAllOrderEnd"))

    return redirect(url_for("order.getAllOrderEnd"))


@order.route("/delete", methods=["GET", "POST"])
@login_required
@view
def deleteOrderEnd(*args ,**kwargs):

    customer_order_id = getCustomerByUserId(session["logged_in"][0])

    if customer_order_id is None:
        customer_order_id = []

    else:

        deleteOrder(customer_order_id[0][0])

    return redirect(url_for("order.getAllOrderEnd"))


