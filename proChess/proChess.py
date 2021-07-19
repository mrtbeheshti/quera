trueTable = {'king': 1,
             'queen': 1,
             'rook': 2,
             'bishop': 2,
             'knight': 2,
             'pawn': 8
             }
king, queen, rook, bishop, knight, pawn = map(int, input().split())
inputTable = {'king': king,
              'queen': queen,
              'rook': rook,
              'bishop': bishop,
              'knight': knight,
              'pawn': pawn
              }
neededPieces = {}
for piece in inputTable:
    neededPieces[piece] = trueTable[piece]-inputTable[piece]
for i in neededPieces:
    print(neededPieces[i], end=" ")
print("\b")
