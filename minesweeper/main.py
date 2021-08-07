row, column = map(int, input().split())
mines = int(input())
table = list()
for i in range(row):
    table.append(["0"] * column)
for n in range(mines):
    x, y = map(int, input().split())
    table[x - 1][y - 1] = "*"
    for i in range(-2, 1):
        for j in range(-2, 1):
            if (
                x + i >= 0
                and x + i < row
                and y + j >= 0
                and y + j < column
                and table[x + i][y + j] != "*"
            ):
                table[x + i][y + j] = str(int(table[x + i][y + j]) + 1)
for i in table:
    print(" ".join(i))
