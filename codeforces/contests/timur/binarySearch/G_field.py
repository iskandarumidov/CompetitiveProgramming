import math

cur = list(input().split())
vp = int(cur[0])
vf = int(cur[1])
a = float(input())

def timeFromPoint(vp, vf, a, x):
  sp = math.sqrt((1-a)**2 + x**2)
  sf = math.sqrt(a**2 + (1-x)**2)
  return (sp/vp) + (sf/vf)

def solve():
  l = 0
  r = 1

  for i in range(50):
    mid1 = l+(r-l)/3
    mid2 = l+2*((r-l)/3)
    if timeFromPoint(vp, vf, a, mid1) < timeFromPoint(vp, vf, a, mid2):
      r = mid2
    else:
      l = mid1
    # print(l, r)
  print(r)

solve()