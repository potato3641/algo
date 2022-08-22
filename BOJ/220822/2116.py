N = int(input())
dices = [] # 0 5, 1 3, 2 4
opps_dice = [5, 3, 4, 1, 2, 0]
max_val = 0
# 0 -> 1,2,3,4
# 1 -> 0,2,4,5
# 2 -> 0,1,3,5
# 3 -> 0,2,4,5
# 4 -> 0,1,3,5
# 5 -> 1,2,3,4
for i in range(N):
    dices.append(list(map(int,input().split())))
first_dice = dices[0]
for i in range(6):
    level = 1
    target = i
    top_dice = [i]
    while len(top_dice) < N:
        target = opps_dice[dices[level].index(dices[level-1][target])]
        top_dice.append(target)
        level += 1
    val = 0
    for j in range(N):
        val += max([dices[j][x] for x in range(6) if x != top_dice[j] and x != opps_dice[top_dice[j]]])
    if max_val < val:
        max_val = val
print(max_val)
