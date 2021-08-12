import json

lines = int(input())
variables = {}
for i in range(lines):
    task = input().replace(" ", "")
    if ":=" in task:
        variable, expression = task.split(":=")
        variables[variable] = json.loads(expression)
    else:
        task=task.replace("print", "")
        startBracket = task.index("[")
        endBracket = task.index("]")
        variable = task[:startBracket]
        index = task[startBracket+1:endBracket]
        print(variables[variable][json.loads(index)])

