
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint

from endpoints.utils import  login_required ,view ,login_required_action

from model.customer import *

customer = Blueprint('customer', __name__, url_prefix='/customer')

@customer.route("/" ,methods=["GET"])
@view
def getAllCustomerEnd(*args, **kwargs):

    customerAll = getAllCustomer()
    if customerAll is None:
        customerAll = []
    return render_template("customer/customers.html", customers = customerAll, **kwargs)

@customer.route("/getEmailAndPassword" ,methods = ["GET"])
@login_required
@view
def getCustomerEmailPasswordEnd( *args, **kwargs):
    email = request.args.get('email', None)
    password = request.args.get('password', None)
    customer = getCustomerByEmailAndPassword(email ,password)
    if customer is None:
        customer = []
    return render_template("customer/customers.html", customers=customer ,**kwargs)


@customer.route("/<id>", methods = ["GET"])
@view
@login_required
def getCustomerByIdEnd(id ,*args ,**kwargs):

    customerById = getCustomerById(id)
    if customerById is None:
        return redirect(url_for("user.feed"))
    else:
        return render_template("customer/customers.html", customerById = customerById[0],**kwargs)


@customer.route("/create", methods = ["GET" ,"POST"])
@login_required
@view
def createCustomerEnd(*args ,**kwargs):
    if request.method == "GET":
        return render_template(("customer/createCustomer.html" ,*kwargs))

    customer_fullname = request.form["customer_fullname"]
    customer_address_id =  request.form["customer_address_id"]
    customer_phone_number =  request.form["customer_phone_number"]
    customer_user_id = request.form["customer_user_id"]
    createCustomer(customer_fullname ,customer_address_id ,customer_phone_number ,customer_user_id)
    return redirect(url_for("customer.getAllCustomerEnd"))


@customer.route("/delete/<id>" ,methods = ["GET" ,"POST"])
@login_required
@view
def deleteCustomerEnd(id ,*args ,**kwargs):
    deleteCustomerById(id)
    return redirect(url_for("customer.getAllCustomers"))


@customer.route("/update/<id>", methods =["GET" ,"POST"])
@login_required
@view
def updateCustomerEnd(id ,*args ,**kwargs):

    customer = getCustomerById(id)
    if request.method == "GET":
        if customer is None:
            redirect(url_for("user.feed"))
        else:
            return render_template("customer/updateCustomer.html", customers= customer)

    customer_fullname = request.form["customer_fullname"]
    customer_address_id = request.form["customer_address_id"]
    customer_phone_number = request.form["customer_phone_number"]
    customer_user_id = request.form["customer_user_id"]

    updateCustomerById(id, customer_fullname, customer_address_id, customer_phone_number, customer_user_id)

    return redirect(url_for('customer.getCustomerByIdEnd', id=id))
