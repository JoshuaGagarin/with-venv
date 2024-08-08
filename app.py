from flask import Flask
import numpy as np


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"