N, L = map(int,input().split())
answerFlag = False
while not answerFlag and L<=100:
    pizet = 1
    while not answerFlag and pizet<=pow(N,0.5)*3:
        if N%pizet != 0:
            pizet += 1
            continue
        value = int(N/pizet)
        if L%2==0: # 짝수
            if value%2==1: # 피연산이 홀수여야함
                Lcnt = L
                if L > 100:
                    continue
                a = int(value/2)
                b = int(value/2)+1
                Lcnt -= 2
                while Lcnt:
                    a -= 1
                    b += 1
                    Lcnt -= 2
                if a < 0:
                    pizet += 1
                    continue
                if sum(x for x in range(a, b+1)) == N:
                    print(*(x for x in range(a, b+1)))
                    answerFlag = True
                    break
                else:
                    pizet += 1
                    continue
        else: # 홀수
            Lcnt = L
            if Lcnt > 100:
                continue
            a = value-1
            b = value+1
            Lcnt -= 3
            while Lcnt:
                a -= 1
                b += 1
                Lcnt -= 2
            if a < 0:
                pizet += 1
                continue
            if sum(x for x in range(a, b+1)) == N:
                print(*(x for x in range(a, b+1)))
                answerFlag = True
                break
            else:
                pizet += 1
                continue
        pizet+= 1
    L += 1
if not answerFlag:
    print(-1)