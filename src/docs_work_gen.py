#!/usr/bin/env python
import requests
import os
import random
import string
import boinc2docker_create_work as b2d

def monolith():
    url_base = "https://api.data.gov/regulations/v3/documents.json?rpp=1000"

    key_file = 'docs_count.txt'
    try:
        file = open(key_file, "r+")
    except FileNotFoundError:
        file = open(key_file, "w+")

    regulations_key = os.environ["REGULATIONS_KEY"]
    work_server_key = os.environ["WORK_SERVER_KEY"]

    current_page = file.readline().replace("\n","")
    if current_page == '':
        current_page = 0
    else:
        current_page = int(current_page)

    if regulations_key != "":
        try:
            record_count = requests.get("https://api.data.gov/regulations/v3/documents.json?api_key=" + regulations_key + "&countsOnly=1").json()["totalNumRecords"]
        except:
            print("Error occured with docs_work_gen regulations API request.")
            return 0

        max_page_hit = record_count // 1000

        while(current_page < max_page_hit):
            url_list = []
            for i in range(1000):
                current_page += 1
                url_full = url_base + "&po=" + str(current_page * 1000)

                url_list.append(url_full)
                if current_page == max_page_hit:
                    break
            random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            requests.post('http://10.76.100.145:5000/add_work', data=dict(job_id=random_id, job_units=url_list, key=work_server_key))
            b2d.boinc2docker_create_work("csdev/boinc:docs", "python app.py " + random_id)


        file_writable = open(key_file, "w")
        file_writable.write(str(current_page))
        file_writable.close()
    else:
        print("No API Key!")


    file.close()

monolith()