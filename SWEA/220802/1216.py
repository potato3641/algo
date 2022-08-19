T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input()
    lines = []
    mosk1 = 0
    mosk2 = 0
    for a in range(2):
        for i in range(100):
            N = 101
            if not a:
                line = input()
                lines.append(line)
            else:
                line = lines[i]
            flag = False
            while not flag:
                N -= 1
                if not N:
                    break
                for adr in range(101-N):
                    if line[adr:N+adr]==line[adr:N+adr][::-1]:
                        if not a and N > mosk1:
                            mosk1 = N
                            flag = True
                            break
                        if a and N > mosk2:
                            mosk2 = N
                            flag = True
                            break
        lines = list(map(list,zip(*lines)))
    mosk = mosk1 if mosk1 > mosk2 else mosk2
    print(f'#{test_case} {mosk}')
    
        
            
    
