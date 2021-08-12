n = int(input())
intervals = []
for i in range(n):
  curInterval = list(map(int, input().split()))
  intervals.append(curInterval)

def solve(intervals):
  intervals.sort()
  ans = [1]*n
  # lastUsed = 
  for i in range(0, n):
    for j in range(i-1, 0, -1):
      if intervals[i][0] >= intervals[j][1]:
        # ans[i] = ans[j]+1
        ans[i] = max(ans[i], ans[j]+1)
  return max(ans)


print(solve(intervals))


# 5
# 1 5
# 2 3
# 3 4
# 0 9
# 0 4