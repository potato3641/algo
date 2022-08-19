T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    line = []
    for i in range(N):
        line.append(int(input()))
    min_tk = 1
    max_tk = max(line)*M
    while min_tk < max_tk: # 이진탐색
        ttl = 0
        mid = (min_tk+max_tk)//2
        for i in range(N):
            ttl += max_tk//line[i]
        if ttl >= M:
            if max_tk-min_tk == 1: # 탐색 끝
                break
            else: # 탐색 범위 반으로 좁히기
                max_tk = mid
        else: # 바로 위에서 반으로 좁힌 범위 중 오른쪽꺼
            gap = max_tk-min_tk+1 # 현재 범위
            min_tk = max_tk # 오른쪽 커서부터 시작
            max_tk += gap # 탐색 범위만큼
    print(f'#{test_case}', max_tk)
