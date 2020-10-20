import urllib.request,json
from .models import Sources,Article

api_key = None

base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_sources(sources):
    get_sources_url = base_url.format(sources,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['articles']:
            sources_results_list = get_sources_response['articles']
            sources_results = process_results(sources_results_list)


    return sources_results
    
def get_article(article):
    get_article_url = base_url.format(article,api_key)
    
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if url:
            article_object = Article( author, title, description, url, urlToImage, publishedAt, content)
            article_results.append(article_object)

    return article_results

def get_article_by_sources(id):
    get_sources_article_url = base_url.format(id,api_key)
    
    
    with urllib.request.urlopen(get_sources_article_url) as url:
        get_sources_article_data = url.read()
        get_sources_article_response = json.loads(get_sources_article_data)

        sources_article_results = None

        if get_sources_article_response['articles']:
            sources_article_results_list = get_sources_article_response['articles']
            sources_article_results = process_results(sources_article_results_list)


    return sources0_article_results

