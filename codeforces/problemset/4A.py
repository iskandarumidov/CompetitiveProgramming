n = int(input())
def solve(n):
  if n < 4:
    print("NO")
    return
  first = n-2
  second = 2
  if first % 2 == 0:
    print("YES")
  else:
    print("NO")
    
solve(n)