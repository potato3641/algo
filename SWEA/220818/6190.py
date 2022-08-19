def is_danjo(a):
    prev = 0
    for i in a:
        if prev > int(i):
            return False
        prev = int(i)
    return True
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = input().split()
    rst = -1
    for i in range(len(line)):
        temp = line[:]
        temp.remove(line[i])
        for j in range(i, len(temp)):
            gop = int(line[i])*int(temp[j])
            if is_danjo(str(gop)) and rst < gop:
                rst = gop
    print(f'#{tc}', rst)
