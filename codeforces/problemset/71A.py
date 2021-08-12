n = int(input())

for i in range(n):
  word = input()
  # print(word)
  if len(word) <= 10:
    print(word)
  else:
    first = word[0]
    last = word[-1]
    num = len(word)-2
    print(first + str(num) + last)


# abcdefghijklmnop

# 5
# abcdefgh
# abcdefghi
# abcdefghij
# abcdefghijk
# abcdefghijklm