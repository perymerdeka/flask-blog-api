import os


class BaseConfig:
    TESTING: bool = False
    SECRET_KEY: str = '@Flaskr-MongoSeCretKeyS'
    DEBUG: bool = False


class DevelopmentConfig(BaseConfig):
    MONGODB_SETTINGS: dict = {
        'db': 'flask_blog_db',
        'host': 'localhost',
        'port': 27017
    }
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class ProductionConfig(BaseConfig):
    pass
