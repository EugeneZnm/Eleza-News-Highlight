from urllib.request import , json

from .models import Sources

api_key = None

base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
