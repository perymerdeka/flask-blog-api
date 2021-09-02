import os

from flask import Flask
from flask_mongoengine import MongoEngine

from projects.blog.api.routes import blog_api_blueprint

db = MongoEngine()


def create_app():
    app = Flask(__name__, static_url_path='')

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # setup extension
    db.init_app(app)

    app.register_blueprint(blueprint=blog_api_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
