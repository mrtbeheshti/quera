length=int(input())
str1=input()
str2=input()
wrong_counter=0
for i in range(length):
    if str1[i]!=str2[i]:
        wrong_counter+=1
print(wrong_counter)