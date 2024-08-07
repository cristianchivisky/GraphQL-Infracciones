from flask import (
    Flask,
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask('MyApp')
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)