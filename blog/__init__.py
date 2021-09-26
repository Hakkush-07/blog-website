from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create Flask app
app = Flask(__name__)
# needed for forms
app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"
# needed for database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# create database
db = SQLAlchemy(app)

from blog import routes
