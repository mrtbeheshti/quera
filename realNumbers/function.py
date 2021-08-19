import re


def real_numbers(numbers):
    result = []
    for i in numbers:
        if re.match(r"^\s*[+-]?[1-9][0-9]*(.[0-9]+)?([eE][+-]?[0-9]+)?\s*$", i):
            result.append("LEGAL")
        else:
            result.append("ILLEGAL")
    return result


print(real_numbers(["1.5e+2", "3.", "1.1.1", "1+e5"]))
