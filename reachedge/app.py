from flask import Flask
app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/users')
def users():
    return 'List of users'
