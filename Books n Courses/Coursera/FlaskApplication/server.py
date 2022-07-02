"""
server.py - A minimal Flask application

Usage: Run `export FLASK_APP=server` followed by `flask run`.

Project: Building an API with Python & Flask

Author: Imdad Ahad
Website: https://imdad.codes
Instagram: https://www.instagram.com/imdadcodes
TikTok: https://www.tiktok.com/@imdadahad
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

