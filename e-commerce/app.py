from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/products')
def product_page():
    items = [
        {"id": 1, "name": "Camiseta", "bar_code": "123456789", "price": 50.00},
        {"id": 2, "name": "Calça", "bar_code": "987654321", "price": 150.00},
        {"id": 3, "name": "Meia", "bar_code": "123123123", "price": 10.00},
        {"id": 4, "name": "Tênis", "bar_code": "456456456", "price": 200.00},
        {"id": 5, "name": "Boné", "bar_code": "789789789", "price": 80.00},
    ]
    return render_template("products.html", items=items)


if __name__ == '__main__':
    app.run()
