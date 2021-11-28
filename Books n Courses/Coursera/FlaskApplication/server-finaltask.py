"""
server.py - A minimal Flask application that connects to a Sqlite Database

Usage: Run `export FLASK_APP=server` and run `flask run`.

Project: Building an API with Python & Flask

Author: Imdad Ahad
Website: https://imdad.codes
Instagram: https://www.instagram.com/imdadcodes
TikTok: https://www.tiktok.com/@imdadahad
"""
from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)



