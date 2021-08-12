n, k = list(map(int, input().split()))
scores = list(map(int, input().split()))

def solve(n, k, scores):
  res = 0
  if scores[k-1] > 0:
    res += k
  else:
    for i in range(k-1, -1, -1):
      if scores[i] > 0:
        return i+1
    return 0
  for i in range(k, len(scores)):
    if scores[i] > 0 and scores[i] == scores[k-1]:
      res+=1
    else:
      break
  return res
    
print(solve(n, k, scores))

# 5 5
# 3 2 1 0 0
