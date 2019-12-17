
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint

from endpoints.utils import  login_required ,view ,login_required_action

from model.firm import *

firm = Blueprint ('firm' ,__name__, url_prefix='/firm')

@firm.route("/" ,methods=["GET"])
@view
def getAllFirmEnd(*args, **kwargs):

    firmAll = getAllFirm()
    if firmAll is None:
        firmAll = []
    return render_template("firm/firms.html", customers = firmAll, **kwargs)

@firm.route("/getEmailAndPassord" ,methods = ["GET"])
@login_required
@view
def getFirmByEmailAndPasswordEnd(*args, **kwargs):

    email = request.args.get('email', None)
    password = request.args.get('password', None)

    firm = getFirmByEmailAndPassword(email, password)
    if firm is None:
        firm = []
    return render_template("firm/firms.html", firms=firm ,**kwargs)


@firm.route("/<id>", methods = ["GET"])
@view
def getFirmByIdEnd(id ,*args ,**kwargs):

    firmById = getFirmById(id)
    if firmById is None:
        return redirect(url_for("user.feed"))
    else:
        return render_template("firm/firms.html", firmById = firmById[0],**kwargs)


@firm.route("/create", methods = ["GET" ,"POST"])
@login_required
@view
def createFirmEnd(*args ,**kwargs):
    if request.method == "GET":
        return render_template(("firm/createFirm.html", *kwargs))

    firm_name = request.form["firm_name"]
    firm_address_id =  request.form["firm_address_id"]
    firm_user_id =  request.form["firm_user_id"]
    firm_phone_number = request.form["firm_phone_number"]
    createFirm(firm_name , firm_address_id , firm_user_id , firm_phone_number)
    return redirect(url_for("firm.getAllFirmEnd"))


@firm.route("/delete/<id>" ,methods = ["GET" ,"POST"])
@login_required
@view
def deleteFirmEnd(id ,*args ,**kwargs):
    deleteFirmById(id)
    return redirect(url_for("firm.getAllFirmEnd"))


@firm.route("/update/<id>", methods =["GET" ,"POST"])
@login_required
@view
def updateCustomerEnd(id ,*args ,**kwargs):

    firm = getFirmById(id)
    if request.method == "GET":
        if firm is None:
            redirect(url_for("user.feed"))
        else:
            return render_template("firm/updateFirm.html", firms= firm)

    firm_name = request.form["firm_name"]
    firm_address_id = request.form["firm_address_id"]
    firm_user_id = request.form["firm_user_id"]
    firm_phone_number = request.form["firm_phone_number"]

    updateFirmById(id,firm_name ,firm_address_id ,firm_user_id ,firm_phone_number)

    return redirect(url_for('firm.getFirmByIdEnd', id = id))
