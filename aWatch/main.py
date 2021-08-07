hour, minute = map(int, input().split())
if hour != 0:
    hour = 12-hour
if minute != 0:
    minute = 60-minute
print("%02d:%02d" % (hour, minute))
