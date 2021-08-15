number = int(input())
counter = 0
sum = 0

for i in range(1, number+1):
    limit = i**(0.5)
    j = 1
    while j <= limit:
        if i % j == 0:
            if j**2 == i:
                sum += j
                counter += 1
            else:
                sum += j
                sum += int(i/j)
                counter += 2
        j += 1
print(counter, sum)
