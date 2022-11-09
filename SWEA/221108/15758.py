def ii(): return int(input())
T = ii()
for tc in range(1, T+1):
    A, B = input().split()
    lenA = len(A)
    lenB = len(B)
    if A in B or B in A:
        if A*lenB == B*lenA:
            print(f'#{tc} yes')
            continue
    print(f'#{tc} no')
