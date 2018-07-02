#!/usr/bin/env python

import sys, os, os.path, tempfile, requests, re

"""
This program does the assimilation for Boinc. 
It creates a master file of squares and adds the results of all of the work to the file.
:return:
"""


def checkFile(filePath):
        """
        Simple checker to see if the file needs to be created or appended to.
        """

        if os.path.exists(filePath): 
                append_write = 'a'
        else: 
                append_write = 'w'

        return append_write


def documents_job(path):
    # file_name = get_file_name(path)

    # Call to make New Job
    # create_work(path) ?
    return 0


def document_job(path):
    file_name = get_file_name(path)

    # Delete job on other server
    r = requests.post("127.0.0.1:420/work_done", job_id="", key="")
    # Save it to Local
    org, docket_id, document_id = get_doc_attributes(file_name)
    local_save(path, org, docket_id, document_id, file)
    os.system("mv " + path + " to/directory")
    # Save it to Fred

    return 0


def get_file_name(path):
    split_path = path.split("/")
    file_name = split_path[len(split_path) - 1]
    return file_name


def get_document_id(file_name):
    doc,id,ending = file_name.split(".")
    return id


def create_new_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        pass


def local_save(path, file, destination):

    if os.path.exists(path):
        os.system("mv " + path + " " + destination)

def get_doc_attributes(file_name):
    document_id = file_name.split(".")

    split_name = re.split("[-_]", document_id[1])

    length = len(split_name)

    document_number = split_name[-1]
    org = split_name[0]
    docket_number = split_name[length - 2]


if __name__ == "__main__":
    if sys.argv[1] != '--error':

        tar_file = sys.argv[1]
        PATH = tempfile.mkdtemp()
        PATHstr = str(PATH)

        # Unzip the tar file and then remove the tar file
        os.system("tar xzf " + tar_file + " --directory " + PATHstr)

        # Create a list of all the files in the directory
        file_list = os.listdir(PATHstr)

        count = 0

        for file in file_list:

            # Documents Checker
            if file.startswith("results"):
                documents_job(PATH + "/" + file)

            # Document Checker
            elif file.startswith("doc."):
                document_job(PATH + "/" + file)
