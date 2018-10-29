from flask import Flask
import os 
import dbinit
import datetime

app = Flask(__name__)

from routes.home import *
from routes.books import *
from routes.auth import *
from routes.errors import * 

if __name__ == "__main__":
    app.secret_key = os.urandom(16)
    app.run(debug=True)
