#CHECK WITH TIMUR
n, k = list(map(int, input().split()))
for i in range(n):
  curCol = list(map(int, input().split()))
  curCol.sort()
  s = curCol[0]
  finished = True
  for j in range(1, k):
    if curCol[j] >= s:
      s+=curCol[j]
    else:
      print("no")
      finished = False
      break
  if finished:
    print("yes")
  

