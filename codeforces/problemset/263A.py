for i in range(5):
  cur = list(map(int, input().split()))
  if 1 in cur:
    print(abs(2-i)+abs(2-cur.index(1)))