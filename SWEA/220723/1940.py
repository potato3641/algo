T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    vel = 0
    rst = 0
    for i in range(N):
        precmd = input()
        if len(precmd) > 1:
            cmd = list(map(int,precmd.split()))
        else:
            cmd = []
        if len(cmd) !=0:
            if cmd[0] == 1:
                vel += cmd[1]
            else:
                vel -= cmd[1]
                if vel < 0:
                    vel = 0
        #print('loc : ' + str(rst) + ', vel : ' + str(vel))
        rst += vel
    print(f'#{test_case} {rst}')
