n, t = list(map(int, input().split()))
books = list(map(int, input().split()))

def solve(n,t, books):
  # l = 0
  r = 0
  res = 0
  curSum = 0
  for l in range(len(books)):
    while r < len(books) and curSum+books[r] <= t:
      curSum += books[r]
      r+=1
    res = max(res, r-l)
    curSum-=books[l]
    # print(l, r, res)

  return res
    
print(solve(n, t, books))


# 5
# 1 5
# 2 3
# 3 4
# 0 9
# 0 4