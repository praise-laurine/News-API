from flask import render_template
from app import app
from .request import get_source

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news = get_source('general')
    business_news = get_source('business')
    sports_news = get_source('sports')
    technology_news = get_source(technology)
    title = 'Home - Welcome to News Bulletin'
    
    return render_template('index.html', title = title,general=general_news,business=business_news,sports=sports_news,technology_news=technology_news)
    

@app.route('/articles/<id>')
def sourceAticles(id):

    '''
    View the article page function that returns the article details page and its data
    '''

    all_articles = articles_source(id)
    print(all_articles)
    source = id
    return render_template('sourceArticles.html',articles = all_articles, source = source)
 
  

