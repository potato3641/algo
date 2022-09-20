def miis(): return map(int,input().split())
T = int(input())
for tc in range(1, T+1):
    nums = float(input())
    nums = int(nums*(1<<20))
    ans = []
    for _ in range(20):
        ans.append(str(nums&1))
        nums >>= 1
    if '1' in ans[:8]:
        ans = 'overflow'
    else:
        target = 20 - ans.index('1')
        ans = ''.join(ans[::-1][:target])
    print(f'#{tc}', ans)
