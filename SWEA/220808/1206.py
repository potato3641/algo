T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    line = list(map(int,input().split()))
    rst = 0
    for i in range(N-4):
        if line[i+2] > line[i] and line[i+2] > line[i+1] and line[i+2] > line[i+3] and line[i+2] > line[i+4]:
            rst += line[i+2]
            max_line = 0
            for j in line[i:i+5]:
                if j > max_line and j != line[i+2]:
                    max_line = j
            rst -= max_line
        #if max(line[i:i+5]) == line[i+2]:
            #rst += line[i+2]-max(line[i:i+2]+line[i+3:i+5])
    print(f'#{test_case} {rst}')
