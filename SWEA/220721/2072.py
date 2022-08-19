T = int(input())
for test_case in range(1, T + 1):
    line = list(map(int,input().split()))
    rst = 0
    for i in range(len(line)):
        if line[i]%2==1:
            rst += line[i]
    print('#{} {}'.format(test_case,rst))
