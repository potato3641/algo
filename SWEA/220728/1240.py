T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
pw = '0001101#0011001#0010011#0111101#0100011#0110001#0101111#0111011#0110111#0001011'
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    real_line = []
    for i in range(N):
        line = input()[::-1]
        codes = line.find('1')
        if codes != -1:
            real_code = line[codes:codes+56][::-1]
            real_line = []
            for j in range(8):
                real_line.append(pw.find(real_code[j*7:j*7+7])//8)
            if ((real_line[0]+real_line[2]+real_line[4]+real_line[6])*3+real_line[1]+real_line[3]+real_line[5]+real_line[7])%10==0:
                rst = sum(real_line)
            else:
                rst = 0
    print(f'#{test_case} {rst}')
        
            
            
