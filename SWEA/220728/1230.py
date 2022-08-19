T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    P = list(input().split())
    M = int(input())
    F = list(input().split())
    id_flag = ''
    x = 0
    y = 0
    s = []
    for i in range(len(F)):
        #print(F[i], id_flag)
        if F[i] == 'I':
            id_flag = 'I'
            x, y, s = 0, 0, [] 
        elif F[i] == 'D':
            id_flag = 'D'
            x, y, s = 0, 0, []
        else:
            if id_flag != '':
                if id_flag == 'I' or id_flag=='D':
                    x = int(F[i])
                    id_flag += 'X'
                elif id_flag == 'IX':
                    y = int(F[i])
                    id_flag += 'Y'
                elif id_flag == 'DX':
                    y = int(F[i]) + x + 1
                    P = P[:(x+1)] + P[y:]
                    x, y, id_flag = 0, 0, ''
                elif id_flag == 'IXY':
                    y -= 1
                    s += [F[i]]
                    if y < 1:
                        #print(P[(x-1):(x+len(s)+2)])
                        P = P[:(x+1)] + s + P[(x+1):]
                        #print(P[(x-1):(x+len(s)+2)])
                        x, y, s, id_flag = 0, 0, [], ''
                else:
                    continue
    rst = ' '.join(P[1:11])
    print(f'#{test_case} {rst}')
            
