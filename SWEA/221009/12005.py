def miis(): return map(int,input().split())
def ii(): return int(input())
def gcd(a, b):
    while b:
        temp = a%b
        a = b
        b = temp
    if a==1:
        return True
    return False
def funcf(n, m):
    cnt = 0
    i = n
    while True:
        i += 1
        if gcd(i, n):
            cnt += 1
            if cnt == m:
                return i
T = ii()
gap = 2*3*5*7*11*13*17*19*23*29*31*37*41*43*47
gap = funcf(gap, 100) - gap
for tc in range(1, T+1):
    K, M = miis()
    target = K-gap
    if target <= 0:
        target = 1
    while (funcf(target, M)-target)^target != K:
        target += 1
        if target > K+gap:
            target = -1
            break
    print(f'#{tc}', target)
