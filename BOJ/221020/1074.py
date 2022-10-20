N, r, c = map(int,input().split())
rst = 0
while N != 0:
    saboon = 0
    if r//(1<<(N-1)) > 0: # hols
        saboon += 2
        r -= (1<<(N-1))
    if c//(1<<(N-1)) > 0: # hols
        saboon += 1
        c -= (1<<(N-1))
    rst += saboon*(1<<(2*N-2))
    N -= 1
print(rst)
