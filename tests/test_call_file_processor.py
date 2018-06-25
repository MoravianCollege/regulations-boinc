from api_call_managment import *
from work_accumulator import *
from call_file_processor import *
import tempfile

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


@pytest.fixture()
def workfile_tempdir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname


# PRE PROCESS


def test_successful_call(workfile_tempdir):
    result = process_results({"documents": [
                             {"documentId": "CMS-2005-0001-0001", "attachmentCount": 4},
                             {"documentId": "CMS-2005-0001-0002", "attachmentCount": 999}]},
                             workfile_tempdir)
    # RETURN ??????
    assert result == 2


def test_call_fail_raises_exception(mock_req):
    mock_req.get(add_api_key(base_url), status_code=407, text='{}')
    with pytest.raises(CallFailException):
        process_call(base_url)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        call_file_processor("this/does/not/exist.txt")


def test_empty_json():
    with pytest.raises(BadJsonException):
        process_results("", "")


def test_bad_json_format():
    with pytest.raises(BadJsonException):
        process_results("information: []", "")





