#!/usr/bin/env python

import sys, os, os.path, tempfile, requests

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
    split_path = path.split("/")
    file_name = split_path[len(split_path) - 1]

    # Call to make New Job
    return 0

def document_job(path):
    split_path = path.split("/")
    file_name = split_path[len(split_path) - 1]
    r = requests.get("127.0.0.1:420")
    # Save it to Local
    # Save it to Fred
    return 0


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
