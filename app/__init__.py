from flask import Flask
from .storage import TaskStorage

def create_app():
    app = Flask(__name__)
    app.config["STORAGE"] = TaskStorage()
    from .routes import bp
    app.register_blueprint(bp)
    return app