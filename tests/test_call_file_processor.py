from api_call_managment import *
from work_accumulator import *
from call_file_processor import *

import pytest
import requests_mock

from api_call import add_api_key

key = os.environ['API_TOKEN_REGULATIONS_GOV']
base_url = 'https://api.data.gov:443/regulations/v3/documents.json?'


'''
def ignore_test_call_file_processor():
    assert call_file_processor()

'''


@pytest.fixture
def mock_req():
    with requests_mock.Mocker() as m:
        yield m


# PRE PROCESS

'''
def ignore_test_successful_call():
    process_call()
    pass
'''


def test_call_fail_raises_exception(mock_req):
    mock_req.get(add_api_key(base_url), status_code=407, text='{}')
    with pytest.raises(CallFailException):
        process_call(base_url)


def ignore_test_file_not_found():
    call_file_processor()
    pass

# PROCESS


def ignore_test_empty_json():
    process_results()
    pass


def ignore_test_bad_json_format():
    process_results()
    pass


def ignore_test_wa_integration():
    process_results()
    pass
