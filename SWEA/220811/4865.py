T = int(input())
for test_case in range(1, T + 1):
    A, B = input(), input()
    temp1 = *A,
    temp2 = *B,
    A, B = set(temp1), list(temp2)
    C = dict()
    for i in A:
        C[i] = 0
    for i in B:
        try:
            C[i] += 1
        except: pass
    max_val = 0
    for i in C:
        if max_val < C[i]:
            max_val = C[i]
    print(f'#{test_case} {max_val}')
            
