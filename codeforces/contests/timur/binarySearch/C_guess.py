r = int(input())+1
l = 0

for i in range(30):
  m = l+(r-l)//2
  print(m)
  res = int(input())
  if res == 0:
    break
  elif res == 1:
    l = m
  elif res == -1:
    r = m

# 5
# -1
# 1
# 0
