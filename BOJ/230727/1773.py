from collections import defaultdict
N, C = map(int,input().split())
mydict = defaultdict(int)
for _ in range(N):
    target = int(input())
    for i in range(1, C//target+1):
        mydict[i*target] = 1
print(len(mydict))
