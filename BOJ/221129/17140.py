def miis(): return map(int,input().split())
def ii(): return int(input())
R, C, K = miis()
A = [list(miis())for _ in range(3)]
def calR():
    result = []
    for line in A:
        result_line = []
        numOrder = set()
        numDict = dict()
        for num in line:
            if num == 0:
                continue
            if num not in numOrder:
                numOrder.add(num)
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        result_line_temp = []
        for i in numOrder:
            result_line_temp.append((i, numDict[i]))
        result_line_temp.sort(key=lambda x: (x[1], x[0]))
        for a, b in result_line_temp:
            result_line.append(a)
            result_line.append(b)
        result.append(result_line[:100])
    max_size = max(len(x) for x in result)
    for i in range(len(result)):
        result[i] += [0]*(max_size - len(result[i]))
    return result
if len(A) >= R and len(A[0]) >= C and A[R-1][C-1] == K:
    print(0)
else:
    timer = 0
    done = False
    while timer < 100:
        if len(A) >= len(A[0]):
            A = calR()
        else:
            A = list(map(list,zip(*A)))
            A = list(map(list,zip(*calR())))
        timer += 1
        if len(A) >= R and len(A[0]) >= C and A[R-1][C-1] == K:
            done = True
            break
    if timer == 100 and not done:
        timer = -1
    print(timer)
