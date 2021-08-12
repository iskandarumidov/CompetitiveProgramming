k = 4
matrix = []
for i in range(k):
  curLength = int(input())
  arr = list(map(int, input().split()))
  arr.sort()
  matrix.append(arr)

def shouldContinue(matrix, pointers):
  for i in range(len(pointers)):
    if pointers[i] >= len(matrix[i]):
      return False
  return True

def findMin(matrix, pointers):
  res = 999999999999999999
  resIndex = -1
  for i in range(len(matrix)):
    if matrix[i][pointers[i]] < res:
      res = matrix[i][pointers[i]]
      resIndex = i
  return resIndex

def solve(matrix):
  pointers = [0]*len(matrix)
  diff = 999999999999999999
  resArr = []
  while shouldContinue(matrix, pointers):
    minValue = min([matrix[i][pointers[i]] for i in range(len(pointers))])
    maxValue = max([matrix[i][pointers[i]] for i in range(len(pointers))])

    if maxValue - minValue < diff:
      diff = maxValue  - minValue
      resArr = [matrix[i][pointers[i]] for i in range(len(pointers))]
    
    minIndex = findMin(matrix, pointers)
    pointers[minIndex]+=1
  return resArr

print(*solve(matrix))


# 6
# 1 10 17 12 15 2

# 5
# 1 2 3 4 5
# 4
# 1 3 4 5
# 4
# 3 4 6 8
# 5
# 2 3 4 6 8
