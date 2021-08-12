from collections import deque

# n = int(input())
# firstQueue = deque(list(map(int, input().split())))
# secondQueue = deque(list(map(int, input().split())))

def balance(front, back):
  while len(front) > len(back):
    back.appendleft(front.pop())
  while len(front) < len(back):
    front.append(back.popleft())

def solve():
  n = int(input())
  front = deque()
  back = deque()

  for i in range(n):
    cur = list(input().split())
    # print(cur)
    if cur[0] == "+":
      back.append(cur[1])
    elif cur[0] == "*":
      front.append(cur[1])
    else:
      print(front.popleft())
    balance(front, back)
    # print(front, back)



solve()


# 10
# + 1
# * 2
# * 3
# + 4
# + 5
# * 6
# * 7
# * 8
# + 9
# + 10