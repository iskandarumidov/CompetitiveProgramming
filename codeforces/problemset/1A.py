from math import ceil

n, m, a = list(map(int, input().split()))

def solve(n, m, a):
  needN = ceil(n/a)
  needM = ceil(m/a)


  return needN*needM
    
print(solve(n, m, a))


# 5
# 1 5
# 2 3
# 3 4
# 0 9
# 0 4