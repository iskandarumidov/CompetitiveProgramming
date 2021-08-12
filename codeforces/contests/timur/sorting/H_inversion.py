n = int(input())
a = list(map(int, input().split()))

# global count
count = 0

def merge(a, b):
  i = 0
  j = 0
  res = []
  global count

  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      res.append(a[i])
      i+=1
    else:
      res.append(b[j])
      count += len(a)-i
      j+=1
  
  while i < len(a):
    res.append(a[i])
    i+=1
  while j < len(b):
    res.append(b[j])
    j+=1
  return res

def mergeSort(a):
  if len(a) <= 1:
    return a
  left = a[:len(a)//2]
  right = a[len(a)//2:]

  left = mergeSort(left)
  right = mergeSort(right)

  return merge(left, right)
  

mergeSort(a)
print(count)