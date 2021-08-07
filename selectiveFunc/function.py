from math import factorial as fact


def comb(n, k):
    return fact(n)/(fact(k)*fact(n-k)) if n >= k else 0
