import work_file as wf

dirpath = ""
filecount = 1


def work_accumulator(dir_path):
    global dirpath, filecount
    dirpath = dir_path
    wf.work_file(dir_path + "results0000.txt")
    filecount = 1


def get_count():
    return filecount


def get_size():
    return wf.size()


def end():
    if get_size() > 0:
        wf.write()


def add_doc(document_id, totalCount):
    global filecount
    if wf.size() + totalCount > 1000:
        wf.write()
        wf.work_file(dirpath + "results" + str("{:0>4d}").format(filecount) + ".txt")
        filecount += 1
        wf.add_doc(document_id, totalCount)


    else:
        wf.add_doc(document_id, totalCount)
