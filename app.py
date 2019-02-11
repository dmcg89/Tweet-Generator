from flask import Flask
import histogram, re, string
app = Flask(__name__)

@app.route('/')
def index:
