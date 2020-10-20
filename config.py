import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = '5136884436074293b9fd97e1a6c1032d'
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/everything?q={}&apiKey={}'
    SECRET_KEY = 'Bih20'
    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    

config_options = {
'development':DevConfig,
'production':ProdConfig

}