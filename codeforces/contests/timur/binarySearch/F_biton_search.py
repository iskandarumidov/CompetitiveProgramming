
# n = int(input())
# k =
# cur = list(input().split())
n, k = map(int, input().split())
data = list(map(int, input().split()))
queries = list(map(int, input().split()))

def findInflection():
  res = 0
  resVal = -999999999999999999999
  for i in range(len(data)):
    if data[i] > resVal:
      resVal = data[i]
      res = i
  return res
  # l = -1
  # r = len(data)
  # while l+1<r:
  #   mid1 = l + (r-l)//3
  #   mid2 = l + 2*((r-l)//3)
  #   # print(l, r)
  #   if data[mid2] > data[mid1]:
  #     l = mid1
  #   else:
  #     r = mid2
  # if data[r] > data[l]:
  #   return r
  # return l

def binSearchIncr(l, r, x):
  while l+1<r:
    mid = l+(r-l)//2
    if data[mid] < x:
      l = mid
    else:
      r = mid
  # return r < len(data) and data[r] == x
  return r


def binSearchDecr(l, r, x):
  while l+1<r:
    mid = l+(r-l)//2
    if data[mid] < x:
      r = mid
    else:
      l = mid
  # return l > 0 and data[l] == x
  return l

def solve():
  inflection = findInflection()
  for cur in queries:
    incr = binSearchIncr(-1, inflection, cur)
    decr = binSearchDecr(inflection-1, len(data), cur)

    if incr < len(data) and data[incr] == cur:
      print("YES", str(data[incr-1]) if incr > 0 else "")
      continue
    if decr > 0 and data[decr] == cur:
      print("YES", str(data[decr-1]) if decr > 0 else "")
      continue
    print("NO")


solve()