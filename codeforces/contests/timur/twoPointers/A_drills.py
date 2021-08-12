n, m = list(map(int, input().split()))
drills = list(map(int, input().split()))
dyubels = list(map(int, input().split()))

def solve(n, m, drills, dyubels):

  i = 0
  j = 0
  res = 9999999999999
  while i < len(drills) and j < len(dyubels):
    res = min(res, abs(drills[i]-dyubels[j]))
    if drills[i] < dyubels[j]:
      i+=1
    else:
      j+=1
    
  return res

print(solve(n, m, drills, dyubels))


# 5
# 1 5
# 2 3
# 3 4
# 0 9
# 0 4