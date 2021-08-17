# quantifiv=cation variables
username = input()
content = input()
validUsername = True
validContent = True

# check username validation
if username.isdigit():
    validUsername = False
validCharsCounter = 0

# detecting invalid characters
for i in content:
    if not (i.isalnum() or i == " "):
        validCharsCounter += 1

# check content validation
if len(content) < (2 * validCharsCounter) and ("spam" in content.lower()):
    validContent = False

# print correct output
if validUsername and validContent:
    print("Not Spam")
elif validUsername and not validContent:
    print("Invalid Content")
elif not validUsername and validContent:
    print("Invalid Sender")
else:
    print("Fully Invalid")
