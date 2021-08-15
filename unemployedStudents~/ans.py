import re

def checkPossibility(insertedStr,calculatedStr):
    insertedStr=insertedStr.split('#')
    pattern= insertedStr[0]+"[0-9]+"+insertedStr[1]
    if re.match(pattern,calculatedStr):
        return True
    return False

def solve(s):
    exp = re.split(r"[\+=]", s)
    num1=exp[0].replace(' ','')
    num2=exp[1].replace(' ','')
    result=exp[2].replace(' ','')
    index = 0
    passiveExp=str()
    isPossible=bool()
    for i in exp:
        if re.match(r".*\#.*", i):
            index = exp.index(i)
    if index==2:
        passiveExp=str(int(num1)+int(num2))
        isPossible= checkPossibility(result,passiveExp)
        result=passiveExp
    elif index==1:
        passiveExp=str(int(result)-int(num1))
        isPossible= checkPossibility(num2,passiveExp)
        num2=passiveExp
    else:
        passiveExp=str(int(result)-int(num2))
        isPossible= checkPossibility(num1,passiveExp)
        num1=passiveExp
    return (num1+' + '+num2+' = '+result) if isPossible else '-1'
