T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int,input().split())
    least_val = A+B-N if A*B and A+B>N else 0
    print(f'#{test_case} {min(A,B)} {least_val}')
