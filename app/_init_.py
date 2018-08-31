# import flask bootstrap
from flask_bootstrap import Bootstrap

# import config options
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    """
    creating application factory function
    :param config_name:
    :return:
    """
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    """
    import app configurations using fom object method
    """