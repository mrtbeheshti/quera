num = int(input())
emlpoyees={}
for i in range(num):
    name,family=input().split()
    emlpoyees[name]=emlpoyees.get(name,0)+1
print(max(list(emlpoyees.values())))