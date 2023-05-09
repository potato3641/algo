N, M, B = map(int,input().split())
line = list(tuple(map(int,input().split())) for _ in range(N))
goal = max(max(x) for x in line)
minval, mingoal = float('inf'), float('inf')

while 0 <= goal:
    target1 = sum(sum((x-goal)*2 for x in y if x > goal) for y in line)
    target2 = sum(sum((goal-x) for x in y if x < goal) for y in line)
    if target2 > B+(target1//2):
        goal -= 1
        continue
    rst = target1+target2
    if minval > rst:
        minval = rst
        mingoal = goal+0
    else:
        break
    goal -= 1
print(minval, mingoal)
