str = input()
green, yellow, red = 0, 0, 0
for c in str:
    if c == 'G':
        green += 1
    elif c == 'Y':
        yellow += 1
    else:
        red += 1
if ((red >= 3) or
    (red >= 2 and yellow >= 2) or
        (red+yellow == 5)):
    print("nakhor lite")
else:
    print("rahat baash")
