from flask import render_template, request, redirect, url_for
from ..request import get_sources, get_article
from . import main

# views
@main.route('/')
# view function
def index():
    """
    view root returning the index page and its data
    :return: categories: entertainment, business, health, science and technology
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


@main.route('/sources/<string:id>')
def get_articles(id):
    """
    view articles page function returning the article page and its data

    """
    article = get_article(id)

    title = 'article'

    return render_template('articles.html', title=title, article=article)
