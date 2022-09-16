def miis(): return map(int,input().split())
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(miis()) for _ in range(N)]
    max_len = 0
    min_val = 0
    for i in range(N):
        for j in range(N):
            myq = [(i, j)]
            visited = set()
            visited.add((i, j))
            while len(myq) > 0:
                target = myq.pop()
                y, x = target

                if y>0 and (y-1, x) not in visited and board[y][x]+1 == board[y-1][x]:
                    myq.append((y-1,x))
                    visited.add((y-1,x))
                if x>0 and (y, x-1) not in visited and board[y][x]+1 == board[y][x-1]:
                    myq.append((y,x-1))
                    visited.add((y,x-1))
                if y+1<N and (y+1, x) not in visited and board[y][x]+1 == board[y+1][x]:
                    myq.append((y+1,x))
                    visited.add((y+1,x))
                if x+1<N and (y, x+1) not in visited and board[y][x]+1 == board[y][x+1]:
                    myq.append((y,x+1))
                    visited.add((y,x+1))
                # print(myq, tc)
            if max_len < len(visited):
                max_len = len(visited)
                min_val = board[i][j]
            elif max_len == len(visited):
                if min_val > board[i][j]:
                    min_val = board[i][j]
    print(f'#{tc} {min_val} {max_len}')
