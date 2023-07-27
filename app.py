from flask import Flask, request

from config import Config


def create_app():
    app = Flask(__name__)
    
    # config
    app.config.from_object(Config)


    # blueprint
    from routes import routes_list
    routes_list(app)
    
    return app

