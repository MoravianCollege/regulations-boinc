import requests
import os
import json

key = os.environ['FRED_API_TOKEN_REGULATIONS_GOV']


def call(url):
    result = requests.get(url)
    if (300 <= result.status_code < 400):
        raise TemporaryException
    if(result.status_code == 429): #0 calls remaining
        raise ApiCountZeroException
    if(result.status_code == 403): #Invlaid API key
        raise PermanentException
    if(400 <= result.status_code < 600):
        raise PermanentException

    documents = json.loads(result.text)
    return documents



def add_api_key(url):
    return url + "api_key=" + str(key)


class TemporaryException(Exception):
    print("There seems to be a connection error")

class ApiCountZeroException(Exception):
    print("You have used all your API calls.")

class PermanentException(Exception):
    print("There is an error with your API call")