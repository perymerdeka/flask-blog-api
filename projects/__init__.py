from flask import Flask
from flask_mongoengine import MongoEngine
from projects.blog.views import blog_blueprint

db = MongoEngine()


def create_app():
    app = Flask(__name__, static_url_path='')

    # setup extension
    db.init_app(app)

    # register blueprint
    app.register_blueprint(blueprint=blog_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
