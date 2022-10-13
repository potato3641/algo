def miis(): return map(int,input().split())
def ii(): return int(input())
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
T = ii()
for tc in range(1, T+1):
    N = ii()
    myq = []
    ans = 0
    for _ in range(N):
        x, y, dirs, K = miis()
        myq.append((y*2, x*2, dirs, K))
    terminated = set()
    while myq:
        temp = [t for t in myq if (t[0], t[1]) not in terminated]
        if len(temp)==0:
            break
        terminated = set()
        bombed = set()
        myq = []
        visited = dict()
        for y, x, dirs, K in temp:
            if (y, x) not in terminated:
                if (y+dy[dirs], x+dx[dirs]) not in visited:
                    if -2000 <= y+dy[dirs] <= 2000 and -2000 <= x+dx[dirs] <= 2000:
                        visited[(y+dy[dirs], x+dx[dirs])] = (dirs, K)
                        myq.append((y+dy[dirs], x+dx[dirs], dirs, K))
                else:
                    terminated.add((y+dy[dirs], x+dx[dirs]))
                    bombed.add((y+dy[dirs], x+dx[dirs]))
                    ans += visited[(y+dy[dirs], x+dx[dirs])][1]+K
                    visited[(y+dy[dirs], x+dx[dirs])] = (dirs, 0)
    print(f'#{tc}', ans)
