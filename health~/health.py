grade = int(input())
travel_days = int(input())
if travel_days == 0:
    print("20")
elif(travel_days == 7):
    print(grade)
elif travel_days > grade:
    print(0)
else:
    print(grade-travel_days)
