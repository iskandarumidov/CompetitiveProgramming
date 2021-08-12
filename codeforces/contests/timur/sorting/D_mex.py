n = int(input())
a = list(map(int, input().split()))

def solve(a):
  a.sort()
  if a[0] > 0:
    return 0
  for i in range(len(a)-1):
    if a[i] == a[i+1] or a[i]+1 == a[i+1]:
      continue
    return a[i]+1
  return a[-1]+1

print(solve(a))

# 0 1 2