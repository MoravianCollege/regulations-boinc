from documents_processor import *
import tempfile
from mock import *

import pytest
import requests_mock

from api_call import add_api_key

key = os.environ['API_TOKEN_REGULATIONS_GOV']
base_url = 'https://api.data.gov:443/regulations/v3/documents.json?'


@pytest.fixture
def mock_req():
    with requests_mock.Mocker() as m:
        yield m


@pytest.fixture()
def workfile_tempdir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname


def test_call_file_processor(mock_req, workfile_tempdir):
    mock_req.get(add_api_key(base_url), status_code=200, text='{"documents": '
                                                              '[{"documentId": "CMS-2005-0001-0001", "attachmentCount": 4},\
                                                                {"documentId": "CMS-2005-0001-0002", "attachmentCount": 999}]}')
    with patch("builtins.open", mock_open(read_data=base_url)) as mock_file:
        result = call_file_processor("path/to/open", workfile_tempdir)
        assert result

def test_valid_results(mock_req, workfile_tempdir):
    mock_req.get(add_api_key(base_url), status_code=200, text='{"documents": '
                                                              '[{"documentId": "CMS-2005-0001-0001", "attachmentCount": 4},\
                                                                {"documentId": "CMS-2005-0001-0002", "attachmentCount": 999}]}')
    result = process_results(process_call(base_url), workfile_tempdir)
    assert result


def test_successful_call(mock_req):
    mock_req.get(add_api_key(base_url), status_code=200, text='{}')
    assert process_call(base_url).text == '{}'


def test_call_fail_raises_exception(mock_req):
    mock_req.get(add_api_key(base_url), status_code=407, text='{}')
    with pytest.raises(CallFailException):
        process_call(base_url)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        call_file_processor("this/does/not/exist.txt", "")


def test_empty_json(mock_req):
    mock_req.get(add_api_key(base_url), status_code=200, text='')
    with pytest.raises(BadJsonException):
        process_results(process_call(base_url), "")


def test_bad_json_format(mock_req):
    mock_req.get(add_api_key(base_url), status_code=200, text='{information: [{},{}]}')
    with pytest.raises(BadJsonException):
        process_results(process_call(base_url), "")





