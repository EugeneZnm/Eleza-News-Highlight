import urllib
import urllib.request, json

from .models import Sources

api_key = None

base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']


def process_results(source_list):
    """
    Function processing the movie result and transforms them to list of objects
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
        loop through list of dictionaries using get method padsing in keys
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
            list of movie objects
            
            """
    # return list of movie objects
    return source_source

def get_source(id):
    """
    function to return details of news source
    :param id:
    :return:
    """
    get_source_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)
    """
    creation of url and getting json data from url and converting it to dictionary
    
    """
