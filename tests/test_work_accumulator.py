import pytest
import tempfile
import os

import work_accumulator as wa


@pytest.fixture()
def workfile_tempdir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname


def test_new_work_accumulator(workfile_tempdir):
    wa.work_accumulator(workfile_tempdir)
    assert wa.get_count() == 1
    assert wa.get_size() == 0


def test_terminate_new_work_accumulator(workfile_tempdir):
    wa.work_accumulator(workfile_tempdir)
    wa.terminate()
    assert not os.path.exists(workfile_tempdir + "results0000.txt")


def test_add_doc_same_file(workfile_tempdir):
    wa.work_accumulator(workfile_tempdir)
    wa.add_doc("ID", 1)
    assert wa.get_count() == 1
    assert wa.get_size() == 1


def test_accumulator_process(workfile_tempdir):
    wa.work_accumulator(workfile_tempdir)
    wa.add_doc("ID", 999)
    assert wa.get_size() == 999
    wa.add_doc("ID", 1)
    assert wa.get_size() == 1000
    wa.terminate()
    assert os.path.exists(workfile_tempdir + "results0000.txt")
    assert wa.get_count() == 1


def test_make_new_file(workfile_tempdir):
    wa.work_accumulator(workfile_tempdir)
    wa.add_doc("ID", 999)
    assert wa.get_count() == 1
    assert wa.get_size() == 999
    wa.add_doc("ID", 2)
    assert wa.get_count() == 2
    assert wa.get_size() == 2
    assert os.path.exists(workfile_tempdir + "results0000.txt")


def test_terminate_writes_files(workfile_tempdir):
    wa.work_accumulator(workfile_tempdir)
    for x in range(10):
        wa.add_doc("ID", 999)
    wa.terminate()
    for y in range(10):
        assert os.path.exists(workfile_tempdir + "results"+ str("{:0>4d}").format(y) + ".txt")
    assert wa.get_count() == 10


def test_terminate_writes_no_extra_file(workfile_tempdir):
    wa.work_accumulator(workfile_tempdir)
    for x in range(10):
        wa.add_doc("ID", 1000)
    wa.terminate()
    for y in range(10):
        assert os.path.exists(workfile_tempdir + "results"+ str("{:0>4d}").format(y) + ".txt")
    assert wa.get_count() == 10



