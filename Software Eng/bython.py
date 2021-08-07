import re
variables={}
str='khorooji(4,3)'
print(re.match(r'\(.*\)',str))
def calExp(str):
    if re.match("^[0-9]+$", str):
        return int(str)
    elif str=='voroodi()':
        return int(input())
    op1,op2=map(getInt,str.split('-','+'))
    return op1+op2 if '+' in str else op1-op2

def calOut(str):
    li=map(getInt,re.split(r",\s?.*\s?,",str))
    result=''
    for e in li:
        result+=e+" "
    return result

def calCondition(str):
    op1,op2=map(getInt,str.split('=='))
    return True if op1==op2 else False
