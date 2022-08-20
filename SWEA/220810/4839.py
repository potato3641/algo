T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int,input().split())
    centA = (1+P)//2
    centB = (1+P)//2
    prevA = 1
    prevB = 1
    endA = P+0
    endB = P+0
    cntA = 0
    cntB = 0
    breaker = True
    while breaker:
        if centA > A:
            endA = centA
            centA = (centA+prevA)//2
            cntA += 1
        elif centA < A:
            prevA = centA
            centA = (centA+endA)//2
            cntA += 1
        else:
            breaker = False
        if centB > B:
            endB = centB
            centB = (centB+prevB)//2
            cntB += 1
        elif centB < B:
            prevB = centB
            centB = (centB+endB)//2
            cntB += 1
        else:
            breaker = False
    if cntA > cntB:
        print(f'#{test_case} B')
    elif cntA < cntB:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')
        
        
