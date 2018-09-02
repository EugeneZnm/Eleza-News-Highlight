import urllib
import urllib.request, json

from .models import Sources, Articles

api_key = None

base_url = None

articles_url = None


def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['SOURCES_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']


def get_sources(category):
    """
    Function taking source arguments as categories

    """

    get_sources_url = base_url.format(category, api_key)
    """
    get_sources_url created as a final url for API requests
    
    """
    with urllib.request.urlopen(get_sources_url) as url:
        """
        send request using urllib.request.urlOpen() as a function taking in 
        get_sources_url as a function
        
        """
        get_sources_data = url.read()

        get_sources_response = json.loads(get_sources_data)
        """
        converting json response to dictionary
        
        """

        source_source = None

        if get_sources_response['sources']:
            """
            property sources used to check if response contains any data
            
            """
            source_source_list = get_sources_response['sources']

            source_source = process_results(source_source_list)
            """
            process results function called taking in list of dictionary objects and returning
            list of source objects
            
            """
    # return list of movie objects
    return source_source


def get_article(id):
    """
    function to return details of news source
    :param articles:
    :return:
    """
    get_article_details_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)
    """
    creation of url and getting json data from url and converting it to dictionary

    """
    article_object = None

    if article_details_response['articles']:
        article_object_list = article_details_response['articles']
        article_object = process_articles(article_object_list)

    return article_object


def process_results(source_list):
    """
    Function processing the source result and transforms them to list of objects
    :param source_list: l
    ist of dictionaries containing source details
    :return:
    source_results, a list of source objects
    """

    source_source = []
    """
    list to store source objects

    """
    for source_item in source_list:
        """
        loop through list of dictionaries using get method passing in keys
        to access values

        """
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Sources(id, name, description, url, category, language, country)
        """
        values used to create movie object 

        """
        source_source.append(source_object)

    return source_source


def process_articles(articles_list):
    """
    Function processing the articles results
    :param articles_list:
    :return:
    """
    articles_out = []

    for article_item in articles_list:
        """
        looping through string of dictionaries using get method passing in keys
        to access values
        
        """
        id= article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        pic = article_item.get('urlToImage')
        dates = article_item.get('publishedAt')

        if pic: # if article has image object is created
            article_object = Articles(id, author, title, description, url, pic, dates)
            """
            Values used to create article object
            
            """
            articles_out.append(article_object)
            """
            returning list with articles
            
            """
    return articles_out

