T = int(input())
for tc in range(1,T+1):
    A, B = input().split()
    while A.find(B) != -1:
        A = A.replace(B,' ')
    print(f'#{tc} {len(A)}')
