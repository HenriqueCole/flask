from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "f2f11aebfbabfb3cad60393d"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db = SQLAlchemy(app)
login_manager = LoginManager(app)

bcrypt = Bcrypt(app)
login_manager.init_app(app)

from mercado import routes
