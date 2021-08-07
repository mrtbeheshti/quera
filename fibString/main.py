num = int(input())
index = 0
result = ''
small = 1
big = 1
while index < num:
    if index+1 == big:
        big = small+big
        small = big-small
        result += "+"
    else:
        result += "-"
    index += 1
print(result)
