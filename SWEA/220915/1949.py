def dfs(n, m, area, dist, visited, dig_flag):
# n 좌 m 표 area 등고보드 dist 길이 visited 방문 dif_flag 땅팠니
    todoflag = True # 일 했니
    if n > 0 and (n-1, m) not in visited: # 위에 길 뚫을 수
        if area[n-1][m] < area[n][m]: # 있니
            dfs(n-1, m, area, dist+1, visited+[(n-1, m)], dig_flag)
            todoflag = False
        for dig in range(1,K+1): # 땅 팔 수
            if dig_flag and area[n-1][m]-dig < area[n][m]: # 있니
                temp = []
                for a in range(N):
                    tempin = area[a][:]
                    temp.append(tempin) # temp는 딮 카피
                temp[n-1][m] -= dig # 거기 땅 파
                dfs(n-1, m, temp, dist+1, visited+[(n-1, m)], False)
                # n-1 좌 m 표 temp 등고보드 dist+1 길이 ... dif_flag 땅 팠다
                todoflag = False
    if n+1 < N and (n+1, m) not in visited:
        if area[n+1][m] < area[n][m]:
            dfs(n+1, m, area, dist+1, visited+[(n+1, m)], dig_flag)
            todoflag = False
        for dig in range(1,K+1):
            if dig_flag and area[n+1][m]-dig < area[n][m]:
                temp = []
                for a in range(N):
                    tempin = area[a][:]
                    temp.append(tempin)
                temp[n+1][m] -= dig
                dfs(n+1, m, temp, dist+1, visited+[(n+1, m)], False)
                todoflag = False
    if m > 0 and (n, m-1) not in visited:
        if area[n][m-1] < area[n][m]:
            dfs(n, m-1, area, dist+1, visited+[(n, m-1)], dig_flag)
            todoflag = False
        for dig in range(1,K+1):
            if dig_flag and area[n][m-1]-dig < area[n][m]:
                temp = []
                for a in range(N):
                    tempin = area[a][:]
                    temp.append(tempin)
                temp[n][m-1] -= dig
                dfs(n, m-1, temp, dist+1, visited+[(n, m-1)], False)
                todoflag = False
    if m+1 < N and (n, m+1) not in visited:
        if area[n][m+1] < area[n][m]:
            dfs(n, m+1, area, dist+1, visited+[(n, m+1)], dig_flag)
            todoflag = False
        for dig in range(1,K+1):
            if dig_flag and area[n][m+1]-dig < area[n][m]:
                temp = []
                for a in range(N):
                    tempin = area[a][:]
                    temp.append(tempin)
                temp[n][m+1] -= dig
                dfs(n, m+1, temp, dist+1, visited+[(n, m+1)], False)
                todoflag = False
    if todoflag:
        # 수많은 dfs중에서 어느 방향으로도 가지 못하면 거기가 dfs의 종료지점
        global max_dist
        if max_dist < dist: # 최대값이니?
            # print(visited)
            max_dist = dist
max_dist = 0
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    max_co = []
    max_hi = 0
    max_dist = 0
    for i in range(N):
        for j in range(N):
            if max_hi < board[i][j]:
                max_hi = board[i][j]
                max_co = [(i, j)]
            elif max_hi == board[i][j]:
                max_co += [(i, j)]
	# 최고높이 봉우리 위치 가지고 dfs 돌리기 시작
    # dfs 돌려서 최고 길이 구하기
    for i, j in max_co:
        dfs(i, j, board, 1, [(i, j)], True)
    print(f'#{tc}', max_dist)