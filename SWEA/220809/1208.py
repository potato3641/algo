T = 10
for test_case in range(1, T + 1):
    D = int(input())
    line = list(map(int,input().split()))
    dumps = [0]*100
    rst = 0
    dump_cnt = 0
    for i in line:
        dumps[i-1] += 1
    for i in range(100):
        if D >= dumps[i]:
            D -= dumps[i]
            dump_cnt += dumps[i]
            dumps[i+1] += dumps[i]
        else:
            dump_cnt += D
            dumps[i+1] += dumps[i] - D
            rst -= i
            D = 0
            break
    for i in range(99,-1,-1):
        if dump_cnt >= dumps[i]:
            dump_cnt -= dumps[i]
            D += dumps[i]
            dumps[i-1] += dumps[i]
        else:
            rst += i
            break
    print(f'#{test_case} {rst}')
