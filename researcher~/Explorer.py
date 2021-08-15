import os


def explore(ttype, address):
    result = dict()
    folders = list(os.walk(address))
    for files in folders:
        for file in files[2]:
            if "." + ttype.lower() in file.lower():
                result[files[0]] = result.get(files[0], 0) + 1
    return result
