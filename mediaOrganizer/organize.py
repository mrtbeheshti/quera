import os
import sys
import re, time


def isPhoto(fileName):
    temp = fileName.lower()
    # return True if (".jpg" in temp or ".jpeg" in temp or ".png" in temp) else False
    return True if (re.match(r".+\.(jpe?g|png)$", temp)) else False


def isVideo(fileName):
    temp = fileName.lower()
    return True if (re.match(r".+\.(mp4|avi|3gp|mpeg|mkv|wmv|mov)$", temp)) else False


src, dst = sys.argv[1:]
files = dict()
srcFiles = list(os.walk(src))
for dir in srcFiles:
    for file in dir[2]:
        if isPhoto(file) or isVideo(file):
            f = open(os.path.join(dir[0], file), "rb")
            files[file] = {
                "content": f.read(),
                "lmd": os.path.getmtime(os.path.join(dir[0], file)),
            }
            f.close()
if not os.path.exists(dst):
    os.mkdir(dst)
os.chdir(dst)
for fileName, properties in files.items():
    modificationYear = str(
        time.strptime(time.ctime(properties["lmd"]), "%a %b %d %H:%M:%S %Y").tm_year
    )
    if not os.path.exists(os.path.join(dst, modificationYear)):
        os.mkdir(os.path.join(dst, modificationYear))
    if isVideo(fileName):
        if not os.path.exists(os.path.join(dst, modificationYear, "videos")):
            os.mkdir(os.path.join(dst, modificationYear, "videos"))
        f = open(os.path.join(dst, modificationYear, "videos", fileName), "wb")
        f.write(properties["content"])
        f.close()
    if isPhoto(fileName):
        if not os.path.exists(os.path.join(dst, modificationYear, "photos")):
            os.mkdir(os.path.join(dst, modificationYear, "photos"))
        f = open(os.path.join(dst, modificationYear, "photos", fileName), "wb")
        f.write(properties["content"])
        f.close()
