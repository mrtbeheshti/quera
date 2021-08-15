def printInv():
    num = int(input())
    if num != 0:
        printInv()
        print(num)


printInv()
