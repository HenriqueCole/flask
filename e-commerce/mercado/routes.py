from mercado import app
from flask import render_template, redirect, url_for, flash
from mercado.models import Item, User
from mercado.forms import CadastroForm, LoginForm
from mercado import db
from flask_login import login_user, logout_user, login_required


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/products')
@login_required
def product_page():
    items = Item.query.all()
    return render_template("products.html", items=items)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = CadastroForm()
    if form.validate_on_submit():
        user = User(user=form.user.data,
                    email=form.email.data,
                    passwordcrip=form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("product_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Erro ao cadastrar: {err_msg}', category='danger')
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(user=form.user.data).first()
        if attempted_user and attempted_user.convert_password(
                raw_password=form.password.data
        ):
            login_user(attempted_user)
            flash(
                f'Login successful! Welcome {attempted_user.user}', category='success')
            return redirect(url_for("product_page"))
        else:
            flash('User or password incorrect! Try again', category='danger')
    return render_template("login.html", form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash('Logout successful!', category='success')
    return redirect(url_for("index"))
