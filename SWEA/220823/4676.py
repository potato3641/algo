T = int(input())
for tc in range(1, T+1):
    target = list(input())
    hypen_cnt = int(input())
    line = list(map(int,input().split()))
    for i in range(len(target)+1,-1,-1):
        adder = '-'*line.count(i)
        if adder:
            target.insert(i, adder)
    print(f'#{tc}', ''.join(target))