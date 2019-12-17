from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint
import datetime
from endpoints.utils import login_required, view, login_required_action

from model.address import *

addresses = Blueprint('addresses', __name__, url_prefix='/addresses')


@addresses.route("/", methods=["GET"])
@view
def getAddressesEnd(*args, **kwargs):
    address = getAllAddresses()
    if address is None:
        address = []
    return render_template("address/address.html", addresses=address, **kwargs)


@addresses.route("/<id>", methods=["GET"])
@view
def getAddressByIdEnd(id, *args, **kwargs):
    address = getAddressById(id)
    if address is None:
        return redirect(url_for("user.feed"))
    else:
        return render_template("address/address.html", addresses=address[0], **kwargs)


@addresses.route("/create", methods=["GET", "POST"])
@login_required
@view
def createAddressEnd(*args, **kwargs):
    if request.method == "GET":
        return render_template("address/createAddress.html", **kwargs)

    street_name = request.form["street_name"]
    building_no = request.form["building_no"]
    apartment_no = request.form["apartment_no"]
    locality_name = request.form["locality_name"]
    city = request.form["city"]
    postcode = request.form["postcode"]

    createAddress(street_name, building_no, apartment_no, locality_name, city, postcode)
    return redirect(url_for("addresses.getAddressesEnd"))


@addresses.route("/delete/<id>", methods=["GET", "POST"])
@login_required
@view
def deleteAddressByIdEnd(id, *args, **kwargs):
    deleteAddress(id)
    return (url_for("addresses.getAddressesEnd"))


@addresses.route("/update/<id>", methods=["GET", "POST"])
@login_required
@view
def updateAddressByIdEnd(id, *args, **kwargs):
    address = getAddressById(id)
    if request.method == "GET":
        if address is None:
            redirect(url_for("user.feed"))
        else:
            return render_template("address/updateAddress.html", address=address[0], **kwargs)

    street_name = request.form["street_name"]
    building_no = request.form["building_no"]
    apartment_no = request.form["apartment_no"]
    locality_name = request.form["locality_name"]
    city = request.form["city"]
    postcode = request.form["postcode"]

    updateAddres(id, street_name, building_no, apartment_no, locality_name, city, postcode)

    return redirect(url_for('addresses.getAddressesByIdEnd', id=id))
