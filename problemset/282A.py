n = int(input())
x = 0
for i in range(n):
  cur = input()
  if "+" in cur:
    x+=1
  else:
    x-=1
print(x)