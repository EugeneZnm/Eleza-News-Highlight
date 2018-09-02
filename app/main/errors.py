# importing render template
from flask import render_template

# importing content in main folder
from . import main


@main.app_errorhandler(404)
def four_four(error):
    """
    Fuction rendering a 404 page
    :param error:
    :return:
    """