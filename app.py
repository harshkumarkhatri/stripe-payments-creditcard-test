from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

pub_key = 'pk_test_j5M62wU5aump7Ige6RRL6bG300GBcA0F6i'
secret_key = 'sk_test_ZDdijuYIjxaiLE15uvr0CE7v00E9LxRqoN'

stripe.api_key = secret_key

@app.route('/')
def index():
    return render_template('index.html', pub_key=pub_key)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/pay', methods=['POST'])
def pay():
    
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=199,
        currency='inr',
        description='The Product'
    )

    return redirect(url_for('thanks'))

if __name__ == '__main__':
    app.run(debug=True)