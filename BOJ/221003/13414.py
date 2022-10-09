def miis(): return map(int,input().split())
N, M = miis()
mydict = dict()
for i in range(M):
    target = input()
    mydict[target] = i
temp = sorted(mydict.items(), key=lambda x: x[1])
cnt = 0
for i in temp:
    cnt += 1
    print(i[0])
    if cnt == N:
        break
