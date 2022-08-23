T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    line = list(map(int,input().split()))
    burned = []
    for i in range(N):
        burned.append([i, line[i]])
    i += 1
    pizza_iter = 0
    last_cnt = 0
    while True:
        if burned[pizza_iter][1]:
            burned[pizza_iter][1] //= 2
            last_cnt = 0
        else:
            last_cnt += 1
            if last_cnt >= N:
                break
        if not burned[pizza_iter][1]:
            if i < M:
                burned[pizza_iter] = [i, line[i]]
                i += 1
        pizza_iter = (pizza_iter+1)%N
    print(f'#{tc}', burned[pizza_iter][0]+1)
        
