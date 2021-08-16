def capitalize(names):
    result = list()
    for name in names:
        name = name.split()
        for i in range(len(name)):
            name[i] = name[i].capitalize()
        result.append(" ".join(name))
    return result
