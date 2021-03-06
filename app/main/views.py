from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Sources

# views
@main.route('/')
def index():
    '''
    view root page function that returns the index the page and its data
    '''
    sources = get_sources('sources')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    title = "Home - News Highlighter"



    return render_template('index.html', title=title, sources=sources, sports_sources=sports_sources, technology_sources=technology_sources, entertainment_sources=entertainment_sources)
    
    

@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
    '''
    articles = get_articles(id)
    title = f'NH | {id}'

    return render_template('articles.html', title=title, articles=articles)

# @main.route('/search/<article_name>')
# def articleSearch(article_name):
#     '''
#     View function to display the search results
#     '''

#     search_article_list = article_name.split("")
#     article_name_format = "+".join(search_article_list)
#     searched_articles = searched_articles(article_name_format)
#     title = f'search results for {article_name}'

#     return render_template('search.html', articles = searched_articles)


