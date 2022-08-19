N = int(input())
line = [str(i+1) for i in range(N)]
for i in line:
    cnt = 0
    for j in i:
        if j=='3' or j=='6' or j=='9':
            cnt += 1
    if cnt > 0:
        print('-'*cnt,end='')
    else:
        print(i, end='')
    if i != line[-1]:
        print(' ',end='')
