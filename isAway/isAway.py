

days = {"shanbe": True,
        "1shanbe": True,
        "2shanbe": True,
        "3shanbe": True,
        "4shanbe": True,
        "5shanbe": True,
        "jome": True}

for i in range(3):
    Number = int(input())
    daysSelected = input().split()
    for day in daysSelected:
        days[day] = False
counter = 0
for i in days:
    if days[i] == True:
        counter += 1
print(counter)
