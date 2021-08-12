from collections import deque

n = int(input())
clients = []

for i in range(n):
    clients.append(list(map(int, input().split())))
    clients[i] = [clients[i][0]*60+clients[i][1], clients[i][2], i]

# print(clients)
def minToHour(mins):
  h = mins // 60
  mins = mins % 60
  return [h, mins]

def solve(clients):
  queue = deque()
  # curTime = 0
  lastOut = 0
  res = [0]*len(clients)

  for i in range(len(clients)):
    cur = clients[i]
    while queue and max(lastOut+20, queue[0][0]+20) <= cur[0]:
      lastOut = max(lastOut+20, queue[0][0]+20)
      res[queue[0][2]] = minToHour(lastOut)
      queue.popleft()
    if len(queue) > cur[1]:
      res[i] = minToHour(cur[0])
    else:
      queue.append(cur)
  while queue:
    lastOut = max(lastOut+20, queue[0][0]+20)
    res[queue[0][2]] = minToHour(lastOut)
    queue.popleft()
  for cur in res:
    print(cur[0], cur[1])





solve(clients)