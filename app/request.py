import urllib.request,json

from flask.globals import request
from .models import User,Comment,Blog

def get_quotes():

    response = request.get('http://quotes.stormconsultancy.co.uk/random.json')
    quotes = response.json()

    return quotes