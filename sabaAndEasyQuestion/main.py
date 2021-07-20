import math as m
num, times = map(int, input().split())
for i in range(times):
    num /= 2
print(m.floor(num))
