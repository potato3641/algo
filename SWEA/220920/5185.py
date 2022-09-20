def miis(): return map(int,input().split())
T = int(input())
for tc in range(1, T+1):
    N, nums = input().split()
    nums = int(nums,16)
    len_nums = int(N)*4
    ans = []
    for _ in range(len_nums):
        ans.append(str(nums&1))
        nums >>= 1
    print(f'#{tc}', ''.join(ans[::-1]))
