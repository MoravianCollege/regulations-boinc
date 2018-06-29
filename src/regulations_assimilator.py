#!/usr/bin/env python

import sys, os, os.path, subprocess

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

if sys.argv[1]!='--error':

    tar_file = sys.argv[1]
    PATH = "temp/"

    # Unzip the tar file and then remove the tar file
    os.system("mkdir ~/project/tmp_boincserver/temp")
    os.system("tar xzf " + tar_file + " --directory ~/project/tmp_boincserver/temp")

    # Create a list of all the files in the directory
    file_list = os.listdir(PATH)

    count = 0

    for file in file_list:

        # Documents Checker
        if file.startswith("results") and file.endswith(".txt"):
            # Call to make New Job
            pass

        # Document Checker
        elif file.startswith("doc."):
            # Save it to Local
            # Save it to Fred
            pass
            
        else:
                print("We got something else") 
        
