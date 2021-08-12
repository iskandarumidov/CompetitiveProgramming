def solve():
  n = int(input())
  arr = [-1]*(10**5+1)
  place = [-1]*(10**5+1)
  l = 0
  r = 0

  for i in range(n):
    cur = list(input().split())
    if cur[0] == "1":
      arr[r] = int(cur[1])
      place[int(cur[1])] = r
      r+=1
    elif cur[0] == "2":
      l+=1
    elif cur[0] == "3":
      r-=1
    elif cur[0] == "4":
      print(place[int(cur[1])]-l)
    elif cur[0] == "5":
      print(arr[l])
    # print()
    # print(l, r, cur, arr, place)



solve()

# 1 2 4


# 7
# 1 1
# 5
# 1 3
# 3
# 2
# 1 2
# 4 2
