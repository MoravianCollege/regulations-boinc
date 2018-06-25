import requests
import os

key = os.environ['API_TOKEN_REGULATIONS_GOV']


def call(url):

    """
    Sends an api call to regulations.gov
    Loads the result as json if it is a valid call, otherwise raises exceptions
    When a 300 status code is given, return a temporary exception so the user can retry the api call
    When a 429 status code is given, the user is out of api calls and must wait an hour to make more
    When 400 or 500 status codes are given there is a problem with the api connection

    :param url: the url that will be sued to make the api call
    :return: returns the json format information of the documents

    """

    result = requests.get(add_api_key(url))
    if 300 <= result.status_code < 400:
        raise TemporaryException
    if result.status_code == 429:
        raise ApiCountZeroException
    if 400 <= result.status_code < 600:
        raise PermanentException
    return result


# The api key will not be given in the url so we must add that ourselves
def add_api_key(url):
    return url + "api_key=" + str(key)


# Throw an exception if there is an error communicating
class TemporaryException(Exception):
    print("NOTICE: There seems to be a connection error")


# Throw an exception if the user is out of api calls
class ApiCountZeroException(Exception):
    print("NOTICE: You have used all your API calls.")


# Throw an exception if there is an error with the API call
class PermanentException(Exception):
    print("NOTICE: There is an error with your API call")