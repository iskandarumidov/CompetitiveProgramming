#TODO: TIMUR

n = int(input())
s = input()
res = 0
for i in range(len(s)-1):
  if s[i] == s[i+1]:
    res+=1
print(res)