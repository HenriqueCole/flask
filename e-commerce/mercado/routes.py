from mercado import app
from flask import render_template
from mercado.models import Item
from mercado.forms import CadastroForm


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/products')
def product_page():
    items = Item.query.all()
    return render_template("products.html", items=items)


@app.route("/register")
def register_page():
    form = CadastroForm()
    return render_template("register.html", form=form)
