from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint
import datetime
from endpoints.utils import login_required, view, login_required_action

from model.product import *
from model.dessert import *
from model.drink import *
from model.firm import *

product = Blueprint('product', __name__, url_prefix='/product')

@product.route("/",methods = ["GET"])
@view
@login_required
def getAllProductEnd(*args, **kwargs):


    if session["logged_in"][3] == 1:
        id = session["logged_in"][0]
        print(id)
        firm = getFirmByUserId(id)
        product = getProductsBySupplierId(firm[0][0])
        drink = getDrinksBySupplierId(firm[0][0])
        dessert = getDessertsBySupplierId(firm[0][0])
        if dessert is None:
          dessert = []
        if drink is None:
            drink = []
        if product is None:
            product = []

        return render_template("product/firmproducts.html", products=product, drinks=drink, desserts=dessert, **kwargs)

    else:
        product = getAllProduct()
        dessert = getAllDessert()
        drink   = getAllDrink()
    if product is None:
        product = []
        dessert = []
        drink   = []
    return render_template("product/products.html", products=product, drinks=drink, desserts=dessert, **kwargs)


@product.route("/<id>", methods=["GET"])
@view
def getProductByIdEnd(id,*args,**kwargs):
    product = getProductListById(id)
    if product is None:
        return redirect(url_for("user.feed"))
    else:
        return render_template("product/products.html", products=product[0], **kwargs)

@product.route("/create",methods = ["GET","POST"])
@login_required
@view
def createProductEnd(*args,**kwargs):

    if request.method == "GET":
        return render_template("product/createProduct.html", **kwargs)

    product_name  = request.form["productname"]
    supplier  = getFirmByUserId( session["logged_in"][0])


    product_price = request.form["price"]
    createProduct(product_name, supplier[0][0], product_price)

    return redirect(url_for("product.getAllProductEnd"))

@product.route("/createDessert",methods = ["GET","POST"])
@login_required
@view
def createDessertEnd(*args,**kwargs):

    if request.method == "GET":
        return render_template("product/createDessert.html", **kwargs)

    dessert_name  = request.form["dessertname"]
    supplier  = getFirmByUserId( session["logged_in"][0])


    product_price = request.form["price"]
    createDessert(dessert_name, supplier[0][0], product_price)

    return redirect(url_for("product.getAllProductEnd"))

@product.route("/createDrink",methods = ["GET","POST"])
@login_required
@view
def createDrinkEnd(*args,**kwargs):

    if request.method == "GET":
        return render_template("product/createDrink.html", **kwargs)

    drink_name  = request.form["drinkname"]
    supplier  = getFirmByUserId(session["logged_in"][0])


    product_price = request.form["price"]
    createDrink(drink_name, supplier[0][0], product_price)

    return redirect(url_for("product.getAllProductEnd"))

@product.route("/delete/", methods =["GET","POST"])
@login_required
@view
def deleteProductByNameEnd( *args, **kwargs):
    if request.method == "GET":
        return render_template("product/deleteproducts.html", **kwargs)
    name = request.form["productname"]
    supplier  = getFirmByUserId( session["logged_in"][0])

    product = deleteProductByName(name, supplier[0][0])

    return redirect(url_for("product.getAllProductEnd"))


@product.route("/deleteDessert", methods =["GET", "POST"])
@login_required
@view
def deleteDessertByNameEnd( *args, **kwargs):
    if request.method == "GET":
        return render_template("product/deletedesserts.html", **kwargs)
    name = request.form["dessertname"]
    supplier  = getFirmByUserId( session["logged_in"][0])

    dessert = deleteDessertByName(name, supplier[0][0])

    return redirect(url_for("product.getAllProductEnd"))

@product.route("/deleteDrink", methods =["GET","POST"])
@login_required
@view
def deleteDrinkByNameEnd( *args, **kwargs):
    if request.method == "GET":
        return render_template("product/deletedrinks.html", **kwargs)
    name = request.form["drinkname"]
    supplier  = getFirmByUserId( session["logged_in"][0])

    drink = deleteDrinkByName(name, supplier[0][0])

    return redirect(url_for("product.getAllProductEnd"))

@product.route("/update", methods=["GET", "POST"])
@login_required
@view
def updatePriceByNameEnd( *args, **kwargs):
    if request.method == "GET":
        return render_template("product/updateproducts.html", **kwargs)
    price = request.form["price"]
    name  = request.form["productname"]
    supplier  = getFirmByUserId( session["logged_in"][0])

    product = updateProductByName(price, name, supplier[0][0])

    return redirect(url_for("product.getAllProductEnd"))


@product.route("/updateDessert", methods=["GET", "POST"])
@login_required
@view
def updateDessertPriceByNameEnd( *args, **kwargs):
    if request.method == "GET":
        return render_template("product/updatedesserts.html", **kwargs)
    price = request.form["price"]
    name  = request.form["dessertname"]
    supplier  = getFirmByUserId( session["logged_in"][0])

    dessert = updateDessertByName(price, name, supplier[0][0])

    return redirect(url_for("product.getAllProductEnd"))

@product.route("/updateDrink", methods=["GET", "POST"])
@login_required
@view
def updateDrinkPriceByNameEnd( *args, **kwargs):
    if request.method == "GET":
        return render_template("product/updatedrinks.html", **kwargs)
    price = request.form["price"]
    name  = request.form["drinkname"]
    supplier  = getFirmByUserId( session["logged_in"][0])

    dessert = updateDrinkByName(price, name, supplier[0][0])

    return redirect(url_for("product.getAllProductEnd"))
