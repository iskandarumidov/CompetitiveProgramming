cur = list(input().split())
n = int(cur[0])
x = int(cur[1])
y = int(cur[2])

def isEnoughTime(n, x, y, t):
  if n == 1:
    return t >= x or t >= y
  first = (t-min(x, y))//x
  second = (t-min(x, y))//y
  return first + second + 1 >= n

def solve():
  l = 0
  r = 2*(10**9)+1

  while l+1<r:
    m = l+(r-l)//2
    if isEnoughTime(n, x, y, m):
      r = m
    else:
      l = m
  print(r)

solve()