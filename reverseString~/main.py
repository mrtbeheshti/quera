num = int(input())
words = input().split()
words = words[::-1]
result = ''
for word in words:
    result += word+" "
print(result[:-1])
