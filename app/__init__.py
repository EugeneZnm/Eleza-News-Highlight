# import flask bootstrap
from flask_bootstrap import Bootstrap

# import config options
from config import config_options

from flask import Flask


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
    import app configurations using from object method
    
    """

    bootstrap.init_app(app)
    """
    initialising flask extension with init_app completing extension initialisation
    
    """

    from .main import main as main_blueprint

    """
    import instance created and registering blueprint method 
    """
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    """
    call function and pass app instance
    
    """
    configure_request(app)

    return app
