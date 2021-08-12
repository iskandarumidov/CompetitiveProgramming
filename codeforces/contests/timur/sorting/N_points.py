n, m = list(map(int, input().split()))
sc = []
for i in range(n):
  cur = list(map(int, input().split()))
  sc.append([min(cur[0], cur[1]), 0])
  sc.append([max(cur[0], cur[1]), 2])

points = list(map(int, input().split()))
for i in range(m):
  sc.append([points[i], 1, i])

def solve(sc):
  res = [0]*m
  bal = 0
  sc.sort()
  # print(sc)

  for cur in sc:
    if cur[1] == 0:
      bal+=1
    elif cur[1] == 2:
      bal-=1
    elif cur[1] == 1:
      res[cur[2]] = bal
 
    
  return res

print(*solve(sc))


# 5
# 1 5
# 2 3
# 3 4
# 0 9
# 0 4