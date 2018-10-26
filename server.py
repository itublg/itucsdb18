from flask import Flask
import dbinit
import datetime

app = Flask(__name__)

from routes.home import *
from routes.books import *

if __name__ == "__main__":
    app.run(debug=True)
