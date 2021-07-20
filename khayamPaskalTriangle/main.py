rows = int(input())
triangle = []
for i in range(rows):
    triangle.append([])
    for j in range(i+1):
        if j in [i, 0]:
            triangle[i].append(1)
        else:
            triangle[i].append(triangle[i-1][j]+triangle[i-1][j-1])
        print(triangle[i][j], end=' ')
    print()
