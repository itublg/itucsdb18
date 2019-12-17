"""
This module is for user endpoints
It has CRUD endpoints
"""

from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Blueprint

from endpoints.utils import login_required, view
from model.address import *
from model.firm import *
from model.product import *
from model.customer import *
from model.order import *

user = Blueprint('user', __name__, url_prefix='/user')


@user.route("/feed", methods=["GET"])
@login_required
@view
def feed(*args, **kwargs):

    return render_template("user/feed.html", **kwargs)


@user.route("/profile", methods=["GET"])
@login_required
@view
def profile(*args, **kwargs):

    if session["logged_in"][3] == 1:
        firmname = getFirmByUserId(session["logged_in"][0])
        print("profile:", firmname)
        if firmname is None:
            firmnname = []
            return render_template("user/firmprofile.html", products = [], firmname= firmname, address = [], **kwargs)

        else:
            address = getAddressById(firmname[0][2])
            if address is None:
              address = []

            product = getProductsBySupplierId(firmname[0][0])
            if product is None:
                product = []
            return render_template("user/firmprofile.html", products = product, firmname=firmname[0][1], address = address, **kwargs)

    else:
        customername = getCustomerByUserId(session["logged_in"][0])
        print(customername)
        if customername is None:
            customername = []
            return render_template("user/customerprofile.html", products=[], firmname=[], address=[], **kwargs)
        else:
            address = getAddressById(customername[0][2])
            if address is None:
                address = []
            orders = getOrdersByCustomerId(customername[0][0])
            if orders is None:
                orders = []
                return render_template("user/customerprofile.html", orders=[], customername=customername[0][1],
                                       address=address, **kwargs)

            products  = getProductListById(orders[0][1])

            print( orders)
            print(products)
        return render_template("user/customerprofile.html", orders=products, customername=customername[0][1], address=address,  **kwargs)
