n = int(input())
res = 0
for i in range(n):
  confidence = list(map(int, input().split()))
  if sum(confidence) >= 2:
    res+=1
print(res)

# 5
# 1 5
# 2 3
# 3 4
# 0 9
# 0 4