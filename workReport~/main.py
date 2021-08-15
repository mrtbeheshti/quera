num, volume = map(int, input().split())
bottlesVolume = 0
for i in range(num):
    vi = int(input())
    bottlesVolume += vi
if bottlesVolume < volume:
    print("NO")
else:
    print("YES")
