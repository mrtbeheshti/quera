print(*(x for x in map(int, input().split()[5::6]) if x % 6 == 0))