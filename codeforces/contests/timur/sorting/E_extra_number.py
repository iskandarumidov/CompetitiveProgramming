#CHECK WITH TIMUR
from collections import defaultdict

n = int(input())
hash = defaultdict(int)
for i in range(n):
	curInp = int(input())
	hash[curInp] += 1
	if hash[curInp] == 4:
		del hash[curInp]
for cur in hash:
	print(cur)
	break
print(hash)