def miis(): return map(int,input().split())
def ii(): return int(input())
S = input()
P = input()
cnt = 0
cur = 0
for p in range(len(P)):
    if P[cur:p+1] not in S:
        cur = p
        cnt += 1
else:
    if P[cur:p+1] in S:
        cnt += 1
print(cnt)
