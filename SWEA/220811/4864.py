T = int(input())
for test_case in range(1, T + 1):
    A, B = input(), input()
    len_A, len_B = len(A), len(B)
    rst = 0
    for i in range(len_B-len_A+1):
        if B[i:i+len_A] == A:
            rst = 1
    print(f'#{test_case} {rst}')
        
