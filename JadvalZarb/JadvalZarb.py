a=int(input("enter your number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        print(str(i*j)+" ",end='')
    print("\b")
input()