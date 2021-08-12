from collections import defaultdict

n = int(input())
cows = [list(map(int, input().split())) for i in range(n)]

def isFullDict(fullDict, toCheckDict):
  for cur in fullDict:
    if cur in toCheckDict and toCheckDict[cur] > 0:
      continue
    else:
      return False
  return True

def solve(n, cows):
  types = defaultdict(int)
  for cur in cows:
    types[cur[1]]+=1
  cows.sort()

  curTypes = defaultdict(int)
  r = 0
  res = float("inf")
  # print(cows)
  for l in range(len(cows)):
    while r < len(cows) and not isFullDict(types, curTypes):
      curTypes[cows[r][1]]+=1
      r+=1
    # print(l, r, curTypes)
    if isFullDict(types, curTypes):
      res = min(res, cows[r-1][0]-cows[l][0])
    curTypes[cows[l][1]]-=1
  return res


print(solve(n, cows))


# 6
# 1 10 17 12 15 2
