def miis(): return map(int,input().split())
N, M = miis()
board = [list(miis()) for _ in range(N)]
ans = 0
debugger = False
# 2이상 차이
# down! up! 차이가 2m이상이 아닌 경우
# ! 사이 공간이 m 이상이 아닌 경우
# m번째 전에 up!이 나올 경우
# n-m번째 전에 down!이 나올 경우
for _ in range(2):
    for line in board:
        temp = ''
        flag = False
        for i in range(1, len(line)):
            if abs(line[i]-line[i-1]) > 1:
                flag = True
                break
            elif line[i]+1 == line[i-1]:
                temp += 'd'
            elif line[i]-1 == line[i-1]:
                temp += 'u'
            else:
                temp += 'p'
        if flag:
            if debugger: print('over')
            continue
        for i in range(2*M-1):
            if 'd'+'p'*i+'u' in temp:
                flag = True
                break
        if flag:
            if debugger: print('dppu short')
            continue
        for i in range(M-1):
            if 'd'+'p'*i+'d' in temp:
                flag = True
                break
            if 'u'+'p'*i+'u' in temp:
                flag = True
                break
        if flag:
            if debugger: print('short dist')
            continue
        for i in range(M-1):
            if 'p'*i+'u' in temp[:len('p'*i+'u')]:
                flag = True
                break
            if 'd'+'p'*i in temp[-len('d'+'p'*i):]:
                flag = True
                break
        if flag:
            if debugger: print('short start end')
            continue
        if debugger: print('worked')
        ans += 1
    board = list(map(list,zip(*board)))
print(ans)
