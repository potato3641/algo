import sys
input = sys.stdin.readline
N = int(input())
nodegoto = [None for _ in range(N+1)]
nodeborn = [0 for _ in range(N+1)]
nodefire = []
debugger = False
for i in range(1,N):
    what, many, where = input().split()
    if what == 'S':
        many = int(many)
        nodefire.append(i+1)
    else:
        many = -1*int(many)
    nodeborn[i+1] = many
    nodegoto[i+1] = int(where)
flag = True
for i in range(len(nodefire)):
    fired = nodefire[i]
    pathend = nodefire[i]
    amount = nodeborn[fired]
    while amount and pathend != 1:
        pathend = nodegoto[pathend]
        if nodeborn[pathend] < 0:
            if amount >= -nodeborn[pathend]:
                amount, nodeborn[pathend] = amount+nodeborn[pathend], 0
            else:
                amount, nodeborn[pathend] = 0, nodeborn[pathend]+amount
    nodegoto[fired] = pathend
    if pathend == 1:
        nodeborn[1] += amount
print(nodeborn[1])
