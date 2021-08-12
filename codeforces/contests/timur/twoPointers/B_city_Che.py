n, rad = list(map(int, input().split()))
arr = list(map(int, input().split()))


def solve(n, rad, arr):
  res = 0
  r = 0
  for l in range(n):
    # while r+1 < n and arr[r+1]-arr[l] <= 5:
    while r < n and arr[r]-arr[l] <= rad:
      
      r+=1
    res+=n-r

  return res

print(solve(n, rad, arr))


# 6
# 1 10 17 12 15 2
