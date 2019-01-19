# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    # test route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
