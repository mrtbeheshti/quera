pieces = list(map(int, input().split()))
eaten = [0, 0, 0, 0]
person = 0
while not 0 in pieces:
    # everybody eat a piece and turn moves to next one
    pieces.append(pieces.pop(0)-1)
    eaten[person] += 1
    # in each turn table will turn onclockwise
    pieces.append(pieces.pop(0))
    person += 1
    if person == 4:
        person = 0
for i in eaten:
    print(i, end=" ")
print()
