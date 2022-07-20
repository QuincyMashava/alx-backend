#!/usr/bin/env python3
'''
A basic flask app
'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''
    Config for babel class
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''
    Retrieve the locale for a web page
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''
    The home page function
    '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7000)
