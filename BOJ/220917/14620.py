def miis(): return map(int,input().split())
N = int(input())
board = [list(miis()) for _ in range(N)]
seedboard = []
for i in range(1, N-1):
    for j in range(1, N-1):
        seedboard.append((i, j))
min_rst = -1
min_temp = set()
for y, x in seedboard:
    visited1 = set()
    visited1.add((y, x))
    visited1.add((y+1, x))
    visited1.add((y-1, x))
    visited1.add((y, x+1))
    visited1.add((y, x-1))
    for yy, xx in [i for i in seedboard if i not in visited1]:
        visited2 = set(visited1)
        visited2.add((yy, xx))
        visited2.add((yy+1, xx))
        visited2.add((yy-1, xx))
        visited2.add((yy, xx+1))
        visited2.add((yy, xx-1))
        if len(visited2) != 10:
            continue
        for yyy, xxx in [i for i in seedboard if i not in visited2]:
            visited3 = set(visited2)
            visited3.add((yyy, xxx))
            visited3.add((yyy+1, xxx))
            visited3.add((yyy-1, xxx))
            visited3.add((yyy, xxx+1))
            visited3.add((yyy, xxx-1))
            if len(visited3) != 15:
                continue
            rst = 0
            for i, j in visited3:
                rst += board[i][j]
            if min_rst == -1 or min_rst > rst:
                min_rst = rst
                min_temp = set(visited3)
print(min_rst)
