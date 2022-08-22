N = int(input())
rst = []
max_cnt = 0
for i in range(1,N+1):
    cnt = 2
    prev = N
    max_arr = [prev, i]
    while prev - i >= 0:
        cnt += 1
        temp = prev - i
        max_arr.append(temp)
        prev = i
        i = temp
    if max_cnt < cnt:
        max_cnt = cnt
        rst = max_arr
    elif cnt < max_cnt:
        break
print(max_cnt)
print(*rst)
