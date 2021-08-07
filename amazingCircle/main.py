n, k = map(int, input().split())
person = 1
counter = 0
while person != 1 or counter == 0:
    counter += 1
    person += k
    if person >= n:
        person -= n

print(counter)
