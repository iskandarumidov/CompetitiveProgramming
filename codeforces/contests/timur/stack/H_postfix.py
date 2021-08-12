def solve():
  inp = list(input().split())
  stack = []
  operators = "+-*"

  for cur in inp:
    if cur in operators:
      if cur == "+":
        stack.append(stack.pop() + stack.pop())
      if cur == "*":
        stack.append(stack.pop() * stack.pop())
      if cur == "-":
        stack.append(-stack.pop() + stack.pop())
    else:
      stack.append(int(cur))

  print(stack[0])

# A B C + D * +

solve()
