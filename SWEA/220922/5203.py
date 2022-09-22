def miis(): return map(int,input().split())
def is_run(target):
    temp = [0]*10
    for i in target:
        temp[i] += 1
    for i in range(2, len(temp)):
        if temp[i-2] and temp[i-1] and temp[i]:
            return True
    return False

def is_tri(target):
    for i in range(10):
        if target.count(i) >= 3:
            return True
    return False
T=int(input())
for tc in range(1, T+1):
    line = list(miis())
    p1 = []
    p2 = []
    rst = 0
    if tc!=4: continue
    for i in range(len(line)):
        if i%2: # 1 3 5 7
            p2.append(line[i])
        else: # 0 2 4 6
            p1.append(line[i])
        if i>3:
            if i%2:
                if is_run(p2) or is_tri(p2):
                    rst = 2
                    break
            else:
                if is_run(p1) or is_tri(p1):
                    rst = 1
                    break
    print(f'#{tc}', rst)
