N = int(input())
M = int(input())
line = list(int(input()) for _ in range(M))+[N+1]
memdict = dict()
memdict[0] = 1
memdict[1] = 1
memdict[2] = 2
memdict[3] = 3
memdict[4] = 5
memdict[5] = 8
memdict[6] = 13
answer = 1
startidx = 1
lineidx = 0
def dfs(n):
    if n in memdict:
        return memdict[n]
    target1, target2 = 0, 0
    if n-2 in memdict:
        target2 = memdict[n-2]
    else:
        memdict[n-2] = dfs(n-2)
        target2 = memdict[n-2]
    if n-1 in memdict:
        target1 = memdict[n-1]
    else:
        memdict[n-1] = dfs(n-1)
        target1 = memdict[n-1]
    memdict[n] = target1+target2
    return memdict[n]
while lineidx < M+1:
    num = line[lineidx]-startidx
    if num in memdict:
        answer *= memdict[num]
    else:
        answer *= dfs(num)
    lineidx += 1
    startidx += num+1
print(answer)
