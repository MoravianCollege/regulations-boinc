
total_size = 0
document_ids = []
filename = ""


def work_file(file):
    global filename, document_ids, total_size
    filename = file
    document_ids = []
    total_size = 0


def write():
    with open(filename, 'w+') as f:
        for doc_id in document_ids:
            f.write(doc_id + "\n")


def add_doc(document_id, count):
    global total_size
    total_size += count
    document_ids.append(document_id)


def size():
    return total_size




