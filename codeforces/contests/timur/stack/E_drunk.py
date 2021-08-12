from collections import deque

n = int(input())
firstQueue = deque(list(map(int, input().split())))
secondQueue = deque(list(map(int, input().split())))

# print(first, second)

def firstBeatsSecond(first, second, n):
  if first == 0 and second == n-1:
    return True
  if second == 0 and first == n-1:
    return False
  if first > second:
    return True
  return False

def solve(firstQueue, secondQueue, n):
  for i in range(1, 2*(10**5)+1):
    first = firstQueue.popleft()
    second = secondQueue.popleft()
    if firstBeatsSecond(first, second, n):
      firstQueue.append(first)
      firstQueue.append(second)
    else:
      secondQueue.append(first)
      secondQueue.append(second)
    if len(firstQueue) == 0:
      print("second", i)
      return
    if len(secondQueue) == 0:
      print("first", i)
      return

  print("draw")




solve(firstQueue, secondQueue, n)