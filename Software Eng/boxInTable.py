from math import sqrt
def isPrime(n):
    if n>1:
        for i in range(1,int(sqrt(n))+1):
            if n%i==0 and i!=1:
                return False
    return True
x='x'
y='y'
n,m,k=map(int,input().split())
table=[[0]*(m+1)]
for i in range(n):
    table.append(list(map(int,input().split())))
    table[i+1].insert(0,0)
p={x:1,y:1}
for i in range(k):
    if isPrime(table[p[x]][p[y]]):
        p[x],p[y]=n-p[x]+1,m-p[y]+1
    elif table[p[x]][p[y]]%4==0:
        p[y]+=1
    elif table[p[x]][p[y]]%4==1:
        p[x]+=1
    elif table[p[x]][p[y]]%4==2:
        p[y]-=1
    else:
        p[x]-=1
    if p[x]==0:
        p[x]=n
    elif p[x]==n+1:
        p[x]=1
    if p[y]==0:
        p[y]=m
    elif p[y]==m+1:
        p[y]=1
print(p[x],p[y])