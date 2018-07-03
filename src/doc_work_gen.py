#!/usr/bin/env python
import requests
import boinc2docker_create_work as b2d
import os
import random
import string

work_server_key = os.environ["WORK_SERVER_KEY"]

def build_job(work_list):
    random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    requests.post('http://10.76.100.145:5000/add_work', data=dict(job_id=random_id, job_units=work_list, key=work_server_key))
    b2d.boinc2docker_create_work("csmoco1742/client:latest", "python document_processor.py " + random_id)
