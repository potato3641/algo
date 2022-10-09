def miis(): return map(int,input().split())
def ii(): return int(input())
T = ii()
for tc in range(1, T+1):
    N = ii()
    board = sorted(list(set([input() for _ in range(N)])), key=lambda x:(len(x), x))
    print(f'#{tc}')
    for i in range(len(board)):
        print(board[i])
