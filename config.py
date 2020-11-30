import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=121fa427f0854f19b82d81d3c5f8b5ea'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=121fa427f0854f19b82d81d3c5f8b5ea'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
            pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig

}