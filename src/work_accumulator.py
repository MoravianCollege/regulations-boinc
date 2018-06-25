import work_file as wf

dirpath = ""
filecount = 1


def work_accumulator(dir_path):
    """
    Constructor for the work accumulator
    Sets all of the global variables to their initial states
    :param dir_path: the directory path used for the files to be written to
    :return:
    """
    global dirpath, filecount
    dirpath = dir_path
    wf.work_file(dir_path + "results0000.txt")
    filecount = 1


def get_count():
    """
    :return: the current file count of the work accumulator
    """
    return filecount


def get_size():
    """
    :return: the current size of the work file
    """
    return wf.size()


def terminate():
    """
    This will write the current work file if the current work file's size is greater than zero
    :return:
    """
    if get_size() > 0:
        wf.write()


def add_doc(document_id, total_count):
    """
    This will add the document id and total number of calls needed for the document to the current work file
    If the size of a work file exceeds 1000 calls, the current work file will be written and then
    a new work file will be created and the filecount will be incremented
    Otherwise, it will add the document id and document count to the current work file
    :param document_id: the document id as a string
    :param total_count: this is an integer for the number of calls to collect all information about the given document
    :return:
    """
    global filecount
    if wf.size() + total_count > 1000:
        wf.write()
        wf.work_file(dirpath + "results" + str("{:0>4d}").format(filecount) + ".txt")
        filecount += 1
    wf.add_doc(document_id, total_count)
