from collections import defaultdict
a, b, c = map(int,input().split())
hapdict = defaultdict(int)
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            hapdict[i+j+k] += 1
print(sorted(list(hapdict.items()),key=lambda x: -x[1])[0][0])
