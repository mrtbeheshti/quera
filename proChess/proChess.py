standardPieces = [1, 1, 2, 2, 2, 8]
insertedPieces = list(map(int, input().split()))
neededPieces = []
for i in range(len(standardPieces)):
    neededPieces.append(standardPieces[i]-insertedPieces[i])
np = neededPieces
print(str(np[0])+' '+str(np[1])+' '+str(np[2]) +
      ' '+str(np[3])+' '+str(np[4])+' '+str(np[5]))
