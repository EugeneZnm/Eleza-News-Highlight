from urllib.request import , json

from .models import Sources

api_key = None

base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']


def process_results()


def get_sources(category):
    """
    Funtion taking source arguments as categories

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

        if get_sources_response['sources']
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