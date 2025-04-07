from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name, group='Group 2')

@app.route('/about')
def about():
    message = 'Our names are Aiman, Sami, Serena, Jhaap, and Khrisha. Welcome to our flower shop'
    return render_template('about.html', title='About us', msg=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Example validation logic (you can replace this with your real authentication logic)
        if username == "admin" and password == "password":
            return redirect(url_for('home'))  # Redirect to home if credentials are correct
        else:
            return "Login failed. Please check your credentials."

    return render_template('login.html')  # Render the login form on GET request

def send_contact_message(name, email, message):
    print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    # Additional logic for sending the message or storing it

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_contact_message(name, email, message)  # Function to send message
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/funfacts')
def funfacts():
    return render_template('funfacts.html')