def miis(): return map(int,input().split())
def ii(): return int(input())
T = ii()
for tc in range(1, T+1):
    S = input()
    if len(S) == S.count('0'):
        print(f'#{tc} no')
        continue
    if S.count('1')%2==1:
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')
