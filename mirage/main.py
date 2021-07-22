num = int(input())
results = []
for i in range(num):
    x, y = map(int, input().split())
    if x == y or x == y+2:
        if y % 2 == 0:
            if x == y:
                results.append(y*2)
            else:
                results.append((y+1)*2)
        else:
            if x == y:
                results.append(y*2-1)
            else:
                results.append(y*2+1)
    else:
        results.append(-1)
while len(results) != 0:
    print(results.pop(0))
