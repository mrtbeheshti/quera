distance, length, width = map(int, input().split())
maxlength = int(distance/length)
result=""
for i in range(maxlength, -1, -1):
    remainedDistance=distance-(i*length)
    if(remainedDistance%width==0):
          widthSteps=int(remainedDistance/width)
          result=str(i)+" "+str(widthSteps)
          break
print(result) if result!='' else print(-1)