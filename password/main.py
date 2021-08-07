num = int(input())
password = input()
rotation = 0
for c in password:
    wheel = input()
    rotates = wheel.find(c)
    if 9-rotates < rotates:
        rotates = 9-rotates
    rotation += rotates
print(rotation)
