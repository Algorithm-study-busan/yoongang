n = int(input())

words = []
for _ in range(n):
  word = input()
  words.append(word)

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for word in words:
  print(word)
