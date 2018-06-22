from api_call_managment import *
from work_accumulator import *



def call_file_processor():
    """
    try:
        open file
    except os exception:
        something
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


def process_results(json, dirpath):
    # New Wa
    # find json['documents']
    # Iterate over docs
    # Get id and attachment count
    # add 1 to attach
    # Call WA to add doc
    pass