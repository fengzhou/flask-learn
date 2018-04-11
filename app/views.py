from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hotfix')
def hotfix():
    return "this is a hotfix"

@app.route('/master')
def master():
    return "master"

@app.route('/is2')
def hello():
    return "is2"

