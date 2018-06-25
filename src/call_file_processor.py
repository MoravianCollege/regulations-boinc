from api_call_managment import *
import work_accumulator as wa



def call_file_processor(filepath):
    try:
        f = open(filepath, 'r')
    except FileNotFoundError:
        raise FileNotFoundError

    # HOW TO TEST
    """
    for line in file:
        json = process_call(line)
        process_results(json, dirpath)
    """
    pass


def process_call(url):
    # Call Manager
    try:
        api_call_manager(url)
    # Check for exceptions
    except CallFailException:
        raise CallFailException
    # RETURN SOMETHING


def process_results(json, dirpath):
    try:
        print(json)
        doc_list = json["documents"]
    except TypeError:
        raise BadJsonException

    wa.work_accumulator(dirpath)
    for doc in doc_list:
        wa.add_doc(doc["documentId"], doc["attachmentCount"] + 1)

    # RETURN ??????
    return wa.get_count()


class BadJsonException(Exception):
    print("NOTICE: The Json appears to be formatted incorrectly.")
