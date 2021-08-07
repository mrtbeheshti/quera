str = input()
ls = list()
for i in str:
    if i == "=" and len(ls) > 0:
        ls.pop()
    else:
        ls.append(i)
print("".join(ls))
