T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    Pn = int(input())
    P = list(map(int,input().split()))
    Fn = int(input())
    F = input().split()
    modeflag = ''
    x = 0
    s = []
    for i in range(len(F)):
        if F[i] == 'I':
            modeflag = 'I'
            P = P[:x] + s + P[x:]
            x = 0
            s = []
        elif modeflag == 'I':
            x = int(F[i])
            modeflag = 'IX'
        elif modeflag == 'IX':
            modeflag = 'IXY'
        elif modeflag == 'IXY':
            s.append(int(F[i]))
            if i == len(F)-1:
                P = P[:x] + s + P[x:]
    print(f'#{test_case} ',end='')
    for i in range(10):
        print(f'{P[i]} ',end='')
    print()
            
            
