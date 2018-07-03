#!/usr/bin/env python

import sys, os, os.path, tempfile, requests, re, shutil

from doc_work_gen import build_job

ip = "10.76.100.145:5000"

server_key = os.environ["WORK_SERVER_KEY"]

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


# TODO
def documents_job(path):
    document_ids = []
    with open(path, 'r') as f:
        for line in f:
            doc_id = line.strip()
            document_ids.append(doc_id)
    build_job(document_ids)


def document_job(path):
    save_path = 'root/project/data/'
    local_save(path, save_path)
    # TODO: Save it to Google Storage


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


def get_doc_attributes(file_name):
    document_id = get_document_id(file_name)

    split_name = re.split("[-_]", document_id)
    org = split_name[0]
    if not split_name[1].isdigit():
        org = org + '-' + split_name[1]
    id = split_name[-1]
    docket_id = document_id[:document_id.index(id)-1]
    return org, docket_id, document_id


def local_save(cur_path, destination):
    file_name = get_file_name(cur_path)
    org, docket_id, document_id = get_doc_attributes(file_name)
    destination_path = destination + org + "/" + docket_id + "/" + document_id + "/"
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    shutil.copy(cur_path, destination_path + '/' + file_name)


def remove_job(path):
    with open(path + 'job_id.txt', 'r') as f:
        job_id = f.read().strip()
    r = requests.post(ip + "/work_done?job_id=" + job_id + "&key=" + server_key)
    r.raise_for_status()



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

        remove_job(PATH)