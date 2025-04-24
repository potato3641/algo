from collections import defaultdict
N = int(input())
reldict = defaultdict(set)
cntdict = defaultdict(int)
for num in range(N):
    line = input()
    for i in range(N):
        if line[i] == "Y":
            if i >= num:
                reldict[num].add(i)
                reldict[i].add(num)
            cntdict[num] += 1
ans = 0
for i in range(N):
    stack = [[i, x] for x in reldict[i]]
    visited = {i}
    cnt = 0
    idx = 0
    while idx < len(stack):
        bridge = stack[idx]
        idx += 1
        target = bridge[-1]
        if target not in visited:
            visited.add(target)
            cnt += 1
        for x in reldict[target]:
            if bridge[-2] == x:
                continue
            if x not in visited:
                visited.add(x)
                cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)