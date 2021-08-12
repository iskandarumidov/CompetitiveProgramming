str1 = input()
str2 = input()

i = 0

while i < len(str1):
  c1 = str1[i].lower()
  c2 = str2[i].lower()
  if c1 != c2:
    if c1 > c2:
      print(1)
      break
    else:
      print(-1)
      break 
  i+=1
if i == len(str1):
  print(0)