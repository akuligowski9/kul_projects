"""
server.py - A minimal Flask application demonstrating Blueprints

Usage: Run `export FLASK_APP=server` followed by `flask run`.

Project: Building an API with Python & Flask

Author: Imdad Ahad
Website: https://imdad.codes
Instagram: https://www.instagram.com/imdadcodes
TikTok: https://www.tiktok.com/@imdadahad
"""
from flask import Flask, jsonify, request

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


@app.route("/books", methods=["POST"])
def post_book():
    request_json = request.get_json()
    try:
        title = request_json['title']
        author = request_json['author']
    except KeyError:
        return "Please provide a title and author.", 400

    new_book = {
        "id": books[-1]["id"] + 1,
        "title": title,
        "author": author
    }
    books.append(new_book)

    serialised = {
        "books": books
    }

    return jsonify(serialised)

