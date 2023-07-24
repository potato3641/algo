A, B, C = map(int,input().split())
if C-B:
    answer = A//(C-B)+1
    print(answer if answer > 0 else -1)
else:
    print(-1)
