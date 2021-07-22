import math
numb, maxCap = map(int, input().split())
jars = list(map(int, input().split()))
jams = 0
for i in jars:
    jams += i
print(numb-math.ceil(jams/maxCap))
