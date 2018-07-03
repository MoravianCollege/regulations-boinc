#!/usr/bin/env python
import sys, os, os.path, tempfile

"""
This program is a validator
"""


def file_length_checker(file_name):
    
    result = open(file_name, "r")
    counter = 0

    for line in result:
        counter += 1

    return counter <= 1000


def documents_checker(path):
    file_name = get_file_name(path)

    number = True
    for x in range(7,10):
        try:
            file_name[x].isdigit()
            int(file_name[x])
        except:
            number = False
            break

    if file_name.startswith("results") and number and file_name.endswith(".txt"):
        if file_length_checker(path):
            return 1
    else:
        return 0


def document_checker(path):
    file_name = get_file_name(path)
    split_id = file_name.split("-")
    split_id = split_id[len(split_id) - 1].split(".")
    document_number = split_id[len(split_id) - len(split_id)]
    if file_name.startswith("doc.") and int_checker(document_number):
        return 1
    else:
        return 0


def int_checker(string):
    """
    This is a private function used to check to see if the string passed is an int
    :return:
    """
    for x in range(len(string)):
        try:
            int(string[x])
        except:
            return False
    return True


def get_file_name(path):
    split_path = path.split("/")
    file_name = split_path[len(split_path) - 1]
    return file_name


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

            count += documents_checker(PATHstr + "/" + file)
            count += document_checker(PATHstr + "/" + file)

        if os.path.exists(PATHstr + '/job_id.txt'):
            count += 1

        if count == len(file_list):
            sys.exit(0)

        else:
            sys.exit(1)
