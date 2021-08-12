res = [0, 0, 0]
n = int(input())
for i in range(n):
  cur = list(map(int, input().split()))
  res[0] += cur[0]
  res[1] += cur[1]
  res[2] += cur[2]
if res == [0, 0, 0]:
  print("YES")
else:
  print("NO")