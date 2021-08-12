cur = list(input().split())
w = int(cur[0])
h = int(cur[1])
n = int(cur[2])



def solve():
  l = 0
  r = min(w, h)*(10**9)

  while l+1<r:
    m = l+(r-l)//2
    if n > ((m//h)*(m//w)):
      l = m
    else:
      r = m
    # print(l,)
  print(r)
solve()