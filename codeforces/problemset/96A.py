#TODO: TIMUR
# a = "0123456789"
# print(a[0:0+5])

s = input()
i = 0
wasPrinted = False

if len(s) < 7:
  print("NO")
  wasPrinted = True

while i <= len(s)-7 and not wasPrinted:
  # print(s[i:i+8])
  if s[i:i+7] == "1111111" or s[i:i+7] == "0000000":
    print("YES")
    break
  i+=1
if i == len(s)-6 and not wasPrinted:
  print("NO")


#1111111
# 1000000001
