result = ''
for i in range(5):
    word = input()
    if ('HAFEZ' in word) or ('MOLANA' in word):
        result += str(i+1)+' '
if result == '':
    print("NOT FOUND!")
else:
    print(result)
