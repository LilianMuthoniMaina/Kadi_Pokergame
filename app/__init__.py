from flask import Flask
from app.db import db


def create_app():
    app=Flask(__name__)
    from app.auth import auth_bp
    app.register_blueprint(auth_bp)
    return app