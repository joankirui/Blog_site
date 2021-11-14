import requests,json


# from .models import User,Comment,Blog

def get_quotes():

    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    quotes = response.json()

    return quotes