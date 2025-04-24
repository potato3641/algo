from collections import defaultdict
wordA = input()
wordB = input()
dictA = defaultdict(int)
dictB = defaultdict(int)
ans = 0
for word in wordA:
    dictA[word] += 1
for word in wordB:
    dictB[word] += 1
for word in set(wordA)|set(wordB):
    ans += abs(dictA[word]-dictB[word])
print(ans)