n=int(input())
k=int(input())
str=input()
for i in range(k):
    str=str[-1]+str[:-1]
for i in range(len(str)):
    newchr=ord(str[i])+k
    while newchr>ord('z'):
        newchr= (newchr-ord('z'))+ord('a')-1    
    str=str[:i]+chr(newchr)+str[i+1:]
print(str)