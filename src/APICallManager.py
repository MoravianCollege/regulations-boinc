import time

from APICall import *

key = os.environ['FRED_API_TOKEN_REGULATIONS_GOV']
base_url = 'https://api.data.gov:443/regulations/v3/documents.json?'

def api_call_manager(url):
    pause = 0
    while (pause < 51):
        try:
            document = call(url)
            return document
        except TemporaryException:
            time.sleep(300)
            pause += 1
        except PermanentException:
            break
        except ApiCountZeroException:
            time.sleep(3600)
    raise CallFailException



class CallFailException(Exception):
    print("There is an error with your API call")












