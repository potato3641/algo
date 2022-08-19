yanky = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
T = int(input())
for tc in range(1, T+1):
    tc, N = input().split()
    str_line = input().split()
    num_line = []
    sort_line = []
    for i in str_line:
        num_line.append(yanky.index(i))
    num_line.sort()
    for i in num_line:
        sort_line.append(yanky[i])
    print(f'{tc}')
    print(*sort_line)
