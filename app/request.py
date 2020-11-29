from app import app
import urllib.request,json
from .models import Source

Source = source.Source
# Getting api key
api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url)as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['source']:
            source_results_list = get_source_response['source']
            source_results = process_source(source_results_list)

    return source_results        
        

def process_source(source_list):
    '''
    Function that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dicionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''

    source_results = []
    for source_item in source_list:
        id =  source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')  
        language = source_item.get('language')
        country = source_item.get(country)

        source_object = Source(id,name,description,url,category,language,country)
        source_results.append(source_object)


    return source_results  

def get_articles(article):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    articles_url = art_url.format(article,api_key)
    
    with urllib.request.urlopen(articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_object = None

        if articles_response['articles']:
            articles_object_items = articles_response['articles']
            articles_object = process_articles(articles_object_items)

    return articles_object 


def process_articles(articles_list):
    '''
    '''
    




