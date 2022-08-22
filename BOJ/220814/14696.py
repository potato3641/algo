R = int(input())
for _ in range(R):
    basket = [[0]*4 for _ in range(2)]
    rst = 'D'
    for i in range(2):
        N, *line = map(int,input().split())
        for n in range(N):
            basket[i][line[n]-1] += 1
    for i in range(3,-1,-1):
        if basket[0][i] > basket[1][i]:
            rst = 'A'
            break
        if basket[0][i] < basket[1][i]:
            rst = 'B'
            break
    print(rst)
