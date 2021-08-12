a = list(map(int, input().split()))

def solve(a):
  arr = [0]*101
  res = []

  for cur in a:
    arr[cur] += 1
  for num in range(len(arr)):
    for q in range(arr[num]):
      res.append(num)

  print(*res)

solve(a)