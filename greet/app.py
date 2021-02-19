from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def welcomehome():
    return 'welcome home'

@app.route('/welcome/back')
def welcomeback():
    return 'welcome back'