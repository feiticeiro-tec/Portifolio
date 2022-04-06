from flask import Flask
from servidor.blueprints.portfolio import portfolio

def create_app():
    app = Flask(__name__)
    app.register_blueprint(portfolio)
    return app
