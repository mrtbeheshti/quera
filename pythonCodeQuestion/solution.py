import re


def solve(path):
    lineCounter = int()
    f = open(path, "r")
    while True:
        line = f.readline()
        if not line:
            break
        line = re.sub(r"\s", "", line)

        if line and not line[0] == "#":
            lineCounter += 1
    f.close()
    return lineCounter


print(solve("in.py"))
