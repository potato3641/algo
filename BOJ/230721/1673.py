while True:
    try:
        target = input()
    except:
        break
    n, k = map(int,target.split())
    cnt = 0
    while n//k:
        cnt += n//k*k
        add = n//k
        n = n%k
        n += add
    print(cnt+n)
