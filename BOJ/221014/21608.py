dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
N = int(input())
hope = [[] for _ in range(N*N+1)]
bluestack = []
for i in range(N*N):
    num, *line = map(int,input().split())
    hope[num] = line
    bluestack.append(num)
batchdict = dict()
rst = 0
for num in bluestack:
    max_cnt = 0
    max_witch = set()
    for i in range(N):
        for j in range(N):
            if (i, j) not in batchdict:
                cnt = 0
                for d in range(4):
                    if (i+dy[d], j+dx[d]) in batchdict and batchdict[(i+dy[d], j+dx[d])] in hope[num]:
                        cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
                    max_witch = {(i, j)}
                elif max_cnt == cnt:
                    max_witch.add((i, j))
    # print('cur1 : ', max_witch)
    if len(max_witch) > 1:
        max_cnt = 0
        max_blank = set()
        for i, j in max_witch:
            if (i, j) not in batchdict:
                cnt = 0
                for d in range(4):
                    if 0<=i+dy[d]<N and 0<=j+dx[d]<N and (i+dy[d], j+dx[d]) not in batchdict:
                        cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
                    max_blank = {(i, j)}
                elif max_cnt == cnt:
                    max_blank.add((i, j))
        max_witch = sorted(list(max_blank), key=lambda x:(x[0],x[1]))
        # print('cur2 : ', max_witch)
        max_witch = max_witch[0]
    else:
        max_witch = max_witch.pop()
    batchdict[max_witch] = num
    # print('rst : ', batchdict)
for i, j in batchdict:
    cnt = 0
    for d in range(4):
        if 0<=i+dy[d]<N and 0<=j+dx[d]<N:
            if batchdict[(i+dy[d], j+dx[d])] in hope[batchdict[(i, j)]]:
                cnt += 1
    if cnt:
        rst += 10**(cnt-1)
print(rst)
