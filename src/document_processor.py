import json
from call_file_processor import *
import urllib.request

base_url = 'https://api.data.gov/regulations/v3/document?documentId='


def document_processor(filepath, dirpath):
    """

    :param filepath:
    :param dirpath:
    :return:
    """


    f = open(filepath)
    '''
    for line in f:
        doc_id, count = line.split()
        # MAKE INTO URL - ADD DOCUMENT ID
        result = process_call(new URL)
        save_document(result, dirpath)
        # get_Extra_Documents ()
            # 1st. Attach
                # process_call
                # Save document
            # 2nd. FileFormats
                # process_call
                # Save document
        



Save_document ()
# f open file in dirpath
# f write result.text
# f close
'''

# Only for json
def save_document(dirpath, json, documentId):
    f = open(dirpath + "/doc." + documentId + ".json" , "w+")
    f.write(json)
    f.close()

# Everything else
def download_document(dirpath, documentId, url):
    type = url.index("contentType") + 12 # STRATEGY PATTERN
    result, headers = urllib.request.urlretrieve(url, filename=dirpath + "/doc." + documentId + "." + url[type:])








def make_doc_url(documentId):
    return base_url + documentId


def get_extra_documents(result):
    extra_formats = extra_attachments = []
    doc_json = load_json(result)
    # Save doc_json
    total_requests = 0
    try:
        extra_formats = doc_json["fileFormats"]
        total_requests += len(extra_formats)
    except KeyError:
        pass
    try:
        extra_attachments = doc_json["attachments"]
        total_requests += len(extra_attachments)
    except KeyError:
        pass

    for extra_doc in extra_formats:
        process_call(str(extra_doc))
        # Save document
    for attachment in extra_attachments:
        attachment_formats = attachment["fileFormats"]
        for a_format in attachment_formats:
            process_call(str(a_format))
            # Save document

    return total_requests





