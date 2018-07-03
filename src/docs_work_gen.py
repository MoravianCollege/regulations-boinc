#!/usr/bin/env python
import requests
import os
import random
import string
import boinc2docker_create_work as b2d


def monolith():
    '''
    Runs the script. This is one monolithic function (aptly named) as the script just needs to be run; however, there is a certain
    point where I we need to break out of the program if an error occurs, and I wasn't sure how exactly sys.exit() would work and whether
    or not it would mess with things outside of / calling this script, so I just made one giant method so I can return when needed.
    :return:
    '''

    url_base = "https://api.data.gov/regulations/v3/documents.json?rpp=1000"

    #The docs_count file keeps track of where we are in regards to the number of things available to download
    key_file = 'docs_count.txt'
    try:
        file = open(key_file, "r+")
    except FileNotFoundError:
        file = open(key_file, "w+")

    regulations_key = os.environ["REGULATIONS_KEY"]
    work_server_key = os.environ["WORK_SERVER_KEY"]

    #Getting where we are in the number of files to be downloaded, from the docs_count file
    current_page = file.readline().replace("\n","")
    if current_page == '':
        current_page = 0
    else:
        current_page = int(current_page)


    if regulations_key != "":
        #Gets number of documents available to downliad
        try:
            record_count = requests.get("https://api.data.gov/regulations/v3/documents.json?api_key=" + regulations_key + "&countsOnly=1").json()["totalNumRecords"]
        except:
            print("Error occured with docs_work_gen regulations API request.")
            return 0

        #Gets the max page we'll go to; each page is 1000 documents
        max_page_hit = record_count // 1000

        '''This loop generates lists of URLs, sending out a job and writing them to the work server every 1000 URLs.
           It will stop and send whatever's left if we hit the max page limit.'''
        while(current_page < max_page_hit):
            url_list = []
            for i in range(1000):
                current_page += 1
                url_full = url_base + "&po=" + str(current_page * 1000)

                url_list.append(url_full)
                if current_page == max_page_hit:
                    break
            #Generates a random ID to send to the work server along with a list of URLs
            random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            #Sends the work to the work server and makes a job for the client
            requests.post('http://10.76.100.145:5000/add_work', data=dict(job_id=random_id, job_units=url_list, key=work_server_key))
            b2d.boinc2docker_create_work("csmoco1742/client:latest", "python documents_processor.py m" + random_id)

        #Saving our new page index
        file_writable = open(key_file, "w")
        file_writable.write(str(current_page))
        file_writable.close()
    else:
        print("No API Key!")


    file.close()

monolith()