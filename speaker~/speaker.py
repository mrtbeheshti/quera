string = input()
for i in range(len(string)):
    temp = ""
    for j in range(i):
        temp += string[i]
    temp += string[i:]
    print(temp)
