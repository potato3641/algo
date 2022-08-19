T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, P = input().split()
    stacks = ['head']
    for i in P:
        if stacks[-1] != i:
        	stacks.append(i)
        else:
            del stacks[-1]
    print(f'#{test_case} ',end='')
    for i in stacks[1:]:
        print(i,end='')
    print()
        
