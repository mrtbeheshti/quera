x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = 0, 0

vertex1 = ((x3-x2)**2)+((y3-y2)**2)
vertex2 = ((x3-x1)**2)+((y3-y1)**2)
vertex3 = ((x2-x1)**2)+((y2-y1)**2)

maxVertex = max(vertex1, vertex2, vertex3)

if maxVertex == vertex1:
    x4 = (x3-(x1-x2))
    y4 = (y3-(y1-y2))
elif maxVertex == vertex2:
    x4 = (x3-(x2-x1))
    y4 = (y3-(y2-y1))
else:
    x4 = (x2-(x3-x1))
    y4 = (y2-(y3-y1))
print(str(x4)+" "+str(y4))
