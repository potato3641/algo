def miis(): return map(int,input().split())
def ii(): return int(input())
T = ii()
for tc in range(1, T+1):
    temp = set()
    ans = 'yes'
    for i in range(8):
        target = list(input())
        if ans == 'no':
            continue
        todo = False
        for j in range(8):
            if target[j]=='O':
                if j not in temp:
                    temp.add(j)
                    if todo:
                        ans = 'no'
                        break
                    todo = True
                else:
                    ans = 'no'
                    break
    if len(temp) != 8:
        ans = 'no'
    print(f'#{tc}', ans)
