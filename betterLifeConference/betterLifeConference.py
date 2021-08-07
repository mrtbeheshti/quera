row, col = map(int, input().split())
dir = ''
moveRow = 0
moveCol = 0
if col > 10:
    dir = "Left"
    moveCol = 20-col+1
else:
    dir = "Right"
    moveCol = col
moveRow = 10-row+1
print(str(dir)+' '+str(moveRow)+' '+str(moveCol))
