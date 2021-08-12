n = int(input())
arr = list(map(int, input().split()))


def solve(n, arr):
  arr.sort()
  res = 0
  r = 0
  for l in range(n):
    # while r+1 < n and arr[r+1]-arr[l] <= 5:
    while r < n and arr[r]-arr[l] <= 5:
      
      r+=1
    # res = max(res, r-l+1)
    res = max(res, r-l)

  return res

print(solve(n, arr))


# 6
# 1 10 17 12 15 2
