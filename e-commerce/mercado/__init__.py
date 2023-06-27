from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "f2f11aebfbabfb3cad60393d"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db = SQLAlchemy(app)

from mercado import routes
