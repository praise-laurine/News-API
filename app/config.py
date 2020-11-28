class Config:
    '''
    General configuration parent class
    '''
    NEWS-API-BASE-URL = 'https://newsapi.org/v2/sources?country=us&category={}&apikey={}'

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




