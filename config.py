import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://uninets:36573934@localhost/blog'
    SECRET_KEY = 'rv8O_BfuRi1WAQYHhhka0g'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'joankirui99@gmail.com'
    MAIL_PASSWORD = '36573934'



class ProdConfig(Config):
    pass
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://uninets:36573934@localhost/blog'
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}