from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_article,get_article_by_sources


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


@main.route('/article', methods=["POST", "GET"])
def article_page():
    if request.method == 'POST':
        search = request.form.get("search")
        article = requests.get_article(search)
    else:
        article = request.get_article("tech")
    return render_template('articles.html', article=article)


@main.route('/article/<id>')
def sources_article(id):
    sources_article = request.get_article_by_sources(id)
    sources = id
    return render_template('display.html', sources_article=sources_article, sources=sources)