import pytest

import regulations_validator as rv

PATH = 'test_files/'


def test_file_checker_500_lines():
    assert rv.file_length_checker(PATH + '500_lines.txt') is True


def test_file_checker_1000_lines():
    assert rv.file_length_checker(PATH + '1000_lines.txt') is True


def test_file_checker_1001_lines():
    assert rv.file_length_checker(PATH + '1001_lines.txt') is False


def test_documents_checker_results0000():
    assert rv.documents_checker(PATH + 'results0000.txt') == 1


def test_documents_checker_bad_beginning():
    assert rv.documents_checker(PATH + 'rseults0000.txt') == 0


def test_documents_checker_bad_middle():
    assert rv.documents_checker(PATH + 'resultsABCD.txt') == 0


def test_documents_checker_bad_ending():
    assert rv.documents_checker(PATH + 'results0000.csv') == 0


def test_document_checker_doc_HHS_OS_2018_0008_29185_html():
    assert rv.document_checker(PATH + 'doc.HHS-OS-2018-0008-29185.html') == 1


def test_document_checker_doc_AHRQ_FRDOC_0001_0035_html():
    assert rv.document_checker(PATH + 'doc.AHRQ_FRDOC_0001-0035.html') == 1


def test_document_checker_bad_beginning():
    assert rv.document_checker(PATH + 'dco.HHS-OS-2018-0008-29185.html') == 0


def test_document_checker_bad_document_number():
    assert rv.document_checker(PATH + 'doc.HHS-OS-2018-0008-ABCDE.html') == 0


def test_document_checker_bad_document_number_special():
    assert rv.document_checker(PATH + 'doc.AHRQ_FRDOC_0001-ABCD.html') == 0