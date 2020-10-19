from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_article,get_article_by_source


@main.route('/')
def index():
    sources = get_sources('trending')
    technology = get_sources('technology')
    politics = get_sources('politics')
    sports = get_sources('sports')
    beauty = get_sources('beauty')
    
    # sources = request.args.get_sources('popularity')
    if sources:
        return render_template('index.html', technology = technology, trending = sources, politics = politics, sports = sports, beauty = beauty)








# @main.route('/articles', methods=["POST", "GET"])
# def articles_page():
#     if request.method == 'POST':
#         search = request.form.get("search")
#         articles = requests.get_articles(search)
#     else:
#         articles = requests.get_articles("tech")
#     return render_template('articles.html', articles=articles)


# @main.route('/article/<id>')
# def source_article(id):
#     source_articles = requests.get_article_by_source(id)
#     source = id
#     return render_template('display.html', source_articles=source_articles, source=source)