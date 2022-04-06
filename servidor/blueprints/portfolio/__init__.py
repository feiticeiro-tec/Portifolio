from flask import Blueprint,render_template,url_for,request
from servidor.functions.get_projects import getListProjects
import os
import requests

path_dir = os.path.dirname(__file__)

portfolio = Blueprint('portfolio',__name__,static_folder='static',template_folder='templates')

@portfolio.route('/')
def index():
    return render_template('index.html',base_url=request.url,destaque='inicio')

@portfolio.route('/projetos')
def projetos():
    return render_template('projetos.html',base_url=request.url,destaque='projetos',projetos=getListProjects())



