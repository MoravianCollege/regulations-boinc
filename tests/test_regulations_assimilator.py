import pytest
import requests_mock
import tempfile
import os

import regulations_assimilator as ra

PATH = 'test_files/'
ip = "127.0.0.1:420"

@pytest.fixture
def mock_req():
    with requests_mock.Mocker() as m:
        yield m

@pytest.fixture()
def workfile_tempdir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname

def test_get_document_id():
    assert ra.get_document_id('doc.mesd-2018-234234-0001.json') == "mesd-2018-234234-0001"

def test_get_document_id_special():
    assert ra.get_document_id('doc.AHRQ_FRDOC_0001-0036.json') == "AHRQ_FRDOC_0001-0036"

def test_get_file_name():
    assert ra.get_file_name(PATH + 'doc.mesd-2018-234234-0001.json') == "doc.mesd-2018-234234-0001.json"

def test_create_new_dir(workfile_tempdir):
    ra.create_new_dir(workfile_tempdir)
    assert os.path.exists(workfile_tempdir)

def test_local_save():
    assert ra.local_save(PATH + 'doc.mesd-2018-234234-0001.json')
    assert os.path.exists(PATH + 'doc.mesd-2018-234234-0001.json')


