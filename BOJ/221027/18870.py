import sys
input = sys.stdin.readline
def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
line = list(miis())
newline = []
for i in range(N):
    newline.append((line[i],i))
newline.sort(key=lambda x:x[0])
cnt = -1
prev = -float('inf')
for val, idx in newline:
    if prev < val:
        cnt += 1
    line[idx] = cnt
    prev = val
print(*line)
