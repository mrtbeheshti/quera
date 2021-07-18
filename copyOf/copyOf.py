num, name = input().split()
num = int(num)
result = ""
for i in range(num):
    result += "copy of "
result += name
print(result)
