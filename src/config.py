class Config:
    SECRET_KEY = 'dev'

class DevelopmentConfig(Config):
    EGINE_URI = 'mysql://root:@127.0.0.1:3307'
    DB_NAME = 'db_citas'
    SQLALCHEMY_DATABASE_URI = f'{EGINE_URI}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
