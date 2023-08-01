from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "6shbvdfgdsgtebvxbnvcxb"
    app.config["ROOT_DIR"] = os.path.abspath(os.curdir)
    print(app.config["ROOT_DIR"])
    # import blueprints
    from .views import views

    # register blueprints
    app.register_blueprint(views, url_prefix="/")

    return app
