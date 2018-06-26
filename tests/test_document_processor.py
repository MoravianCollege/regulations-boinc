import tempfile
from document_processor import *
from call_file_processor import *
from mock import *

import pytest
import requests_mock

from api_call import add_api_key

key = os.environ['API_TOKEN_REGULATIONS_GOV']
base_url = 'https://api.data.gov/regulations/v3/document?documentId='


@pytest.fixture
def mock_req():
    with requests_mock.Mocker() as m:
        yield m


@pytest.fixture()
def workfile_tempdir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        document_processor("this/does/not/exist.txt", "")


def test_make_doc_url():
    assert base_url + 'DOCUMENTID' == make_doc_url('DOCUMENTID')


def test_collect_extra_documents(mock_req):
    mock_req.get(add_api_key(make_doc_url("DOCUMENT")), status_code=200, text='{ "fileFormats": '
                                                                              '["https://api.data.gov/regulations/v3/download?'
                                                                              'documentId=OSHA-H117-2006-0947-0647&'
                                                                              'attachmentNumber=1&contentType=pdf"] }')
    mock_req.get(add_api_key("https://api.data.gov/regulations/v3/download?documentId=OSHA-H117-2006-0947-0647&attachmentNumber=1&contentType=pdf"),
                 status_code=200, text='Document!')
    result = get_extra_documents(process_call(make_doc_url("DOCUMENT")))

    assert result == 1


def test_collect_attachments(mock_req):
    mock_req.get(add_api_key(make_doc_url("DOCUMENT")), status_code=200, text='{ "attachments": [ '
                                                                              '{ "fileFormats": [ '
                                                                              '"https://api.data.gov/regulations/v3/download?documentId=FDA-2015-N-0540-0004&attachmentNumber=1&contentType=msw12", '
                                                                              '"https://api.data.gov/regulations/v3/download?documentId=FDA-2015-N-0540-0004&attachmentNumber=1&contentType=pdf" '
                                                                              '] } ] }')
    mock_req.get(add_api_key(
        "https://api.data.gov/regulations/v3/download?documentId=FDA-2015-N-0540-0004&attachmentNumber=1&contentType=msw12"),
                 status_code=200, text='Document!')
    mock_req.get(add_api_key(
        "https://api.data.gov/regulations/v3/download?documentId=FDA-2015-N-0540-0004&attachmentNumber=1&contentType=pdf"),
                 status_code=200, text='Document!')

    result = get_extra_documents(process_call(make_doc_url("DOCUMENT")))

    assert result == 1


























