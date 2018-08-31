from flask import render_template, request, redirect, url_for
from ..requests import get_sources


# from . import main
# views
@main.route('/')
# view function
def index():
    """
    view root returning the index page and its data
    :return:
    """

    entertainment = get_sources('entertainment')
    general = get_sources('general')
    health = get_sources('health')
    science = get_sources('science')
    technology = get_sources('technology')
    """
    getting movies according to categories
    
    """
    title = 'ELEZA - FRESH OFF THE PRESS'

    # search_sources = request.args.get('source-query')
    # result from get sources function passed to template
    return render_template('index.html', title=title, entertainment=entertainment.sources, general=general.sources,
                           health=health.sources,
                           science=science.sources, technology=technology.sources)


@main.route('/source/<int:id>')
def get_source(id):
    """
    view sources page function returning the sources details page and its data

    """
    source = get_source(id)
    title = f'{source.title}'

    return render_template('source.html', title=title, source=source)
