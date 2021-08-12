#CHECK WITH TIMUR
n, k = list(map(int, input().split()))
minutes = list(map(int, input().split()))

# print(n, k)
# print(minutes)

def solve(minutes, n):
  minutes.sort()
  res = 0
  for cur in minutes:
    # print(cur, res)
    if n-cur >= 0:
      res+=1
      n = n - cur
  return res

print(solve(minutes, n))