"""
server.py - A minimal Flask application with GET book/, GET book/<id>
and POST book/

Usage: Run `export FLASK_APP=server` followed by `flask run`.

Project: Building an API with Python & Flask

Author: Imdad Ahad
Website: https://imdad.codes
Instagram: https://www.instagram.com/imdadcodes
TikTok: https://www.tiktok.com/@imdadahad
"""

from flask import Flask, jsonify

app = Flask(__name__)
books = [
    {
        "id": 1,
        "title": "Dune",
        "author": "Frank Herbert"
    },
    {
        "id": 2,
        "title": "How to Win Friends & Influence People",
        "author": "Dale Carnegie"
    },
    {
        "id": 3,
        "title": "The Giver",
        "author": "Lois Lowry"
    },
]


@app.route("/books", methods=["GET"])
def get_books():
    serialised = {
        "books": books
    }

    return jsonify(serialised)


@app.route("/books/<int:uid>", methods=["GET"])
def get_book(uid):
    book = next(book for book in books if book["id"] == uid)
    return jsonify(book)







