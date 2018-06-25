import time

from api_call import *



def api_call_manager(url):

    """
    If there were no errors, get the json
    If a temporary error occured, sleep for 5 minutes and try again. Do this 50 times, and if it continues to fail, CallFailException
    If a Permanent error occures, throw CallFailException
    If the users ApiCount is zero, sleep for one hour to refresh the calls

    :param url: the url that will be used to make the api call
    :return: returns the json information of the documents
    """

    pause = 0
    while pause < 51:
        try:
            result = call(url)
            return result
        except TemporaryException:
            time.sleep(300)
            pause += 1
        except PermanentException:
            break
        except ApiCountZeroException:
            time.sleep(3600)
    raise CallFailException


class CallFailException(Exception):
    print("NOTICE: There is an error with your API call")












