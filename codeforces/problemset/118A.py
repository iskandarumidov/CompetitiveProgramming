inp = input()
res = ""

vowels = "aoyeui"

for i in range(len(inp)):
  if inp[i].lower() in vowels:
    continue
  else:
    res = res + "." + inp[i].lower()
print(res)