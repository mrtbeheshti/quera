edges = [int(x) for x in input().split()]
if(edges[0]+edges[1]+edges[2] != 180 or
        edges[0]+edges[1] < edges[2] or
        edges[0]+edges[2] < edges[1] or
        edges[1]+edges[2] < edges[0]) and
        (X):
    print("No")
else:
    print("Yes")
