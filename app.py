from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session encryption

# Product data
products = [
    {'id': 1, 'name': 'Product 1', 'description': 'Description of product 1', 'price': 19.99},
    {'id': 2, 'name': 'Product 2', 'description': 'Description of product 2', 'price': 29.99}
]

# User data
users = {'admin': 'admin'}

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('products'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html', error='')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/products')
def products():
    if 'username' in session:
        return render_template('products.html', products=products)
    return redirect(url_for('login'))

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'username' in session:
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            cart = session.get('cart', [])
            cart.append(product)
            session['cart'] = cart
            return redirect(url_for('products'))
    return redirect(url_for('login'))

@app.route('/cart')
def cart():
    if 'username' in session:
        cart = session.get('cart', [])
        return render_template('cart.html', cart=cart)
    return redirect(url_for('login'))

@app.route('/checkout')
def checkout():
    if 'username' in session:
        cart = session.get('cart', [])
        total = sum(product['price'] for product in cart)
        session.pop('cart', None)
        return render_template('checkout.html', total=total)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
