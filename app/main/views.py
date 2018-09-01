from flask import render_template, request, redirect, url_for
from ..request import get_sources, get_source
from . import main


# views
@main.route('/')
# view function
def index():
    """
    view root returning the index page and its data
    :return:
    """

    entertainment = get_sources('entertainment')
    business = get_sources('business')
    health = get_sources('health')
    science = get_sources('science')
    technology = get_sources('technology')
    """
    getting sources according to categories
    
    """
    title = 'ELEZA - FRESH OFF THE PRESS'

    # result from get sources function passed to template
    return render_template('index.html', title=title, entertainment=entertainment, business=business,
                           health=health, science=science, technology=technology)


@main.route('/source/<int:id>')
def get_source(id):
    """
    view sources page function returning the sources details page and its data

    """
    source = get_source(id)
    title = f'{source.title}'

    return render_template('index.html', title=title, source=source)
