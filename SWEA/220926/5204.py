def miis(): return map(int,input().split())
def msort(m):
    if len(m) <= 1:
        return m
    left = m[0:len(m)//2]
    right = m[len(m)//2:len(m)]
    left = msort(left)
    right = msort(right)
    if left[-1] > right[-1]:
        global rst
        rst += 1
    return merge(left[::-1],right[::-1])
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[-1] <= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    if len(left) > 0:
        result.extend(left[::-1])
    if len(right) > 0:
        result.extend(right[::-1])
    return result
rst = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = list(miis())
    rst = 0
    print(f'#{tc}', msort(line)[N//2], rst)

