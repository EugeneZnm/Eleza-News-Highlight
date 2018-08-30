from flask import render_template


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
    science = get_science('science')
    technology = get_technology('technology')

    title = 'ELEZA - FRESH OFF THE PRESS'

    # search_sources = request.args.get('source-query')
    # result from get sources function passed to template
    return render_template('index.html', title = title, entertainment =entertainment.sources, general=general.sources,health=health.sources,
                           science=science.sources,technology=technology.sources)