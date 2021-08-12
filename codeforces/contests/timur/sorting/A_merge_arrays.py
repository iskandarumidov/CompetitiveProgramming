n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

def solve():
  i = 0
  j = 0
  res = []

  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      res.append(a[i])
      i+=1
    else:
      res.append(b[j])
      j+=1
  
  while i < len(a):
    res.append(a[i])
    i+=1
  while j < len(b):
    res.append(b[j])
    j+=1
  print(*res)
  # for cur in res:
  #   print(cur, end=" ")

solve()