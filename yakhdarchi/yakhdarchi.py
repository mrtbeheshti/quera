temperature = int(input())
output = ""
if temperature > 100:
    output = "Steam"
elif temperature < 0:
    output = "Ice"
else:
    output = "Water"
print(output)
