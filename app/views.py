from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to News Bulletin'
    return render_template('index.html', title = title)

@app.route('/articles/<id>')
def sourceAticles(id):

    '''
    View the article page function that returns the article details page and its data
    '''

    return render_template('sourceArticles.html')
 


