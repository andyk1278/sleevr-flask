from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'supadood'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'What a splendid day it is!'
        },
        {
            'author': {'username': 'droopy'},
            'body': 'The Avengers series is so well made imo.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
