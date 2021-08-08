def divs(a):
    i = 1
    while i <= a:
        if a % i == 0:
            yield i
        i += 1