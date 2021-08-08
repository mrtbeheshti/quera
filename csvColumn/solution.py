def process(path):
    inputFile = open(path, "r")
    outputFile = open("ans.csv", "w")
    while True:
        line = inputFile.readline()
        if not line:
            break
        line = list(map(int, line.replace(" ", "").split(",")))
        numsSum = sum(line)
        string = ""
        for num in line:
            string += str(num) + ", "
        string += str(numsSum) + "\n"
        outputFile.write(string)
    outputFile.close()
    inputFile.close()


