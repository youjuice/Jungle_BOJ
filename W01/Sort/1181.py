N = int(input())
words = set([input() for _ in range(N)])

result = sorted(words, key=lambda x: (len(x), x), reverse=False)

for word in result:
    print(word)
