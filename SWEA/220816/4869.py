T = int(input())
def firefunc(n):
    if n==1:
        return 1
    elif n%2:
        return firefunc(n-1)*2-1
    else:
        return firefunc(n-1)*2+1
for tc in range(1, T+1):
    print(f'#{tc}', firefunc(int(input())//10))
