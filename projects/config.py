import os


class BaseConfig:
    TESTING: bool = False
    SECRET_KEY: str = '@Flaskr-MongoSeCretKeyS'
    DEBUG: bool = False


class DevelopmentConfig(BaseConfig):
    MONGODB_SETTINGS: dict = {
        'db': 'flask_blog_db_dev',
        'host': 'mongodb://localhost:27017/flask_blog_db_dev'
    }
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class ProductionConfig(BaseConfig):
    pass
