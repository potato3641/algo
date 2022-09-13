T = int(input())
for tc in range(1, T+1):
    prev = 96
    cnt = 0
    for alpha in input():
        if prev+1 == ord(alpha):
            cnt += 1
        else:
            break
        prev = ord(alpha)
    print(f'#{tc}', cnt)
