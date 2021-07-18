x, y, z = map(int, input().split())
time = 0
counter = 0
while counter < z:
    time += x
    counter += 1
    if counter < z:
        time += y
        counter += 1
print(time)
