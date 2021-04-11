class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:paSswo0rd@pg:5432/foodcourt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:paSswo0rd@pg:5432/foodcourt'


class DevelopmentConfig(Config):
    DEBUG = True
