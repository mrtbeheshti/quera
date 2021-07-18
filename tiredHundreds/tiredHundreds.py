x1 = input()[::-1]
x2 = input()[::-1]
if(x2 < x1):
    print(str(x2)[::-1]+" < "+str(x1)[::-1])
elif x1 < x2:
    print(str(x1)[::-1]+" < "+str(x2)[::-1])
else:
    print(str(x1)[::-1]+" = "+str(x2)[::-1])
