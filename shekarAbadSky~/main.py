row, column = map(int, input().split())
sky = []
starCounter = 0
for i in range(row):
    sky.append(input())
    for j in sky[i]:
        if j == '*':
            starCounter += 1
print(starCounter)
