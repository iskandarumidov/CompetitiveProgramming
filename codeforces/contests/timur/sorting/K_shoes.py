size = int(input())
n = int(input())
if n > 0:
  shoes = list(map(int, input().split()))
else:
  shoes = []


def solve(shoes):
  shoes.sort()
  i = 0
  res = 0
  lastShoe = size-3
  # while i < len(shoes) and shoes[i] < size:
  #   i+=1
  # if i < len(shoes):
  #   lastShoe = shoes[i]
  #   i+=1
  #   res+=1
  # else:
  #   return 0
  # for i in range(len(shoes)):
  while i < len(shoes):
    if shoes[i] >= lastShoe+3:
      lastShoe = shoes[i]
      res+=1
    i+=1
    
  return res

print(solve(shoes))


# 5
# 1 5
# 2 3
# 3 4
# 0 9
# 0 4