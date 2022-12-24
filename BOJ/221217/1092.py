def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
crains = list(miis())
M = ii()
boxes = list(miis())
crains.sort(reverse=True)
boxes.sort(reverse=True)
ans = 0
if max(boxes) > max(crains):
    ans = -1
else:
    while boxes:
        ans += 1
        for c in crains:
            for b in range(len(boxes)):
                if c >= boxes[b]:
                    del boxes[b]
                    break
print(ans)
