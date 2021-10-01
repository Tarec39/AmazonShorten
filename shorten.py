import settings
import requests

BITLY_TOKEN = settings.BITLY_TOKEN

def shortenURL(longUrl):
    url = "https://api-ssl.bitly.com/v3/shorten"
    access_token = BITLY_TOKEN
    query = {
        'access_token' : access_token,
        'longUrl': longUrl
    }

    request = requests.get(url, params=query).json()['data']['url']
    return request