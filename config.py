import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://uninets:36573934@localhost/blog'
    SECRET_KEY = 'rv8O_BfuRi1WAQYHhhka0g'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # email configurations



class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}