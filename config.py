# import os module allowing interaction with os dependent functionality
import os


class Config:
    SOURCES_API_BASE_URL = "https://newsapi.org/v2/sources?category={}&apiKey={}"
    ARTICLES_BASE_URL = "https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}"
    SOURCES_API_KEY = os.environ.get('SOURCES_API_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
