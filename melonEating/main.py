num = int(input())
weights = list(map(int, input().split()))
print(weights.index(max(weights))+1)
