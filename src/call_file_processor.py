from api_call_managment import *
import work_accumulator as wa

import json


def call_file_processor(filepath, dirpath):
    try:
        f = open(filepath, 'r')
    except FileNotFoundError:
        raise FileNotFoundError
    for line in f:
        result = process_call(line)
        process_results(result, dirpath)
    return True


def process_call(url):
    try:
        result = api_call_manager(url)
        return result
    except CallFailException:
        raise CallFailException


def process_results(result, dirpath):
    try:
        docs_json = json.loads(result.text)
        doc_list = docs_json["documents"]
    except json.JSONDecodeError:
        raise BadJsonException
    except TypeError:
        raise BadJsonException

    wa.work_accumulator(dirpath)
    for doc in doc_list:
        wa.add_doc(doc["documentId"], doc["attachmentCount"] + 1)
    wa.terminate()
    return True


class BadJsonException(Exception):
    print("NOTICE: The Json appears to be formatted incorrectly.")
