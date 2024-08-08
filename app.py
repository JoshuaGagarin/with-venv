from flask import Flask, render_template, request, jsonify
import numpy as np

chat_list = []
response_list = []
app = Flask(__name__)

@app.route("/")
# def index():
#     return "Hello World!"

def home():
    return render_template('index.html',todos=chat_list, responses=response_list, zip=zip)