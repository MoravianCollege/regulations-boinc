
total_size = 0
document_ids = []
filename = ""


def work_file(file_path):
    """
    Constructor for the work file. Sets all of the global variables to their initial states.
    :param file_path: This is the path where the file is that will be written to
    :return:
    """
    global filename, document_ids, total_size
    filename = file_path
    document_ids = []
    total_size = 0


def write():
    """
    This function creates the file given and writes all of the document ids in the work file
    :return:
    """
    with open(filename, 'w+') as f:
        for doc_id in document_ids:
            f.write(doc_id + "\n")


def add_doc(document_id, count):
    """
    This adds the document id to the list of ids that will be saved to a file.
    The count is the number of calls necessary to collect all of the data for the specific document id.
    :param document_id: The document id as a string.
    :param count: This is an integer for the number of calls to collect all information about the given document.
    :return:
    """
    global total_size
    total_size += count
    document_ids.append(document_id)


def size():
    """
    :return: This returns the total number of requests necessary to collect all of the
    data from all the current document ids.
    """
    return total_size




