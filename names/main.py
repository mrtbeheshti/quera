numberOfNames = int(input())
max = 0
for i in range(numberOfNames):
    name = input()
    chars = []
    for j in name:
        if not j in chars:
            chars.append(j)
    if len(chars) > max:
        max = len(chars)
print(max)