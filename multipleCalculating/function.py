def calc(a):
    median, avg, Max = 0, 0, 0
    a.sort()
    if len(a) % 2 == 0:
        median = (a[len(a) // 2 - 1] + a[len(a) // 2]) / 2
    else:
        median = a[len(a) // 2]
    avg = sum(a) / len(a)
    Max = max(a)
    return avg, median, Max


print(calc([2, 20, 30, 29]))
