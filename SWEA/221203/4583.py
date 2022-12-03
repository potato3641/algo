def miis(): return map(int,input().split())
def ii(): return int(input())
def minusOne(n):
    return n-1
T = ii()
for tc in range(1, T+1):
    M, K = miis()
    nums = [0, 1, 2, 3, 4, 5, 6]
    board = [tuple(map(minusOne, miis())) for _ in range(M)]
    cycle = nums[:]
    for a, b in board:
        cycle[a], cycle[b] = cycle[b], cycle[a]
    memo = [nums[:]]
    if K > M:
        flag = False
        for _ in range(K//M):
            nums = [nums[x] for x in cycle]
            # print(nums, len(memo))
            if nums not in memo:
                memo.append(nums[:])
            else:
                flag = True
                break
        if flag:
            for _ in range((K//M)%len(memo)):
                nums = [nums[x] for x in cycle]
                # print(nums, len(memo))
    cnt = K%M
    for a, b in board:
        if cnt == 0:
            break
        nums[a], nums[b] = nums[b], nums[a]
        cnt -= 1
    print(f'#{tc}', ''.join(map(str,nums)))
