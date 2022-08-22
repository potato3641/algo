T = int(input())
line = list(map(int,input().split()))
cnt_asc = 0
cnt_desc = 0
max_cnt = 0
prev = -1
for i in line:
    if prev <= i:
        cnt_asc += 1
    else:
        if max_cnt < cnt_asc:
            max_cnt = cnt_asc
        cnt_asc = 1
    if prev >= i:
        cnt_desc += 1
    else:
        if max_cnt < cnt_desc:
            max_cnt = cnt_desc
        cnt_desc = 1
    prev = i
if max_cnt < cnt_asc:
    max_cnt = cnt_asc
if max_cnt < cnt_desc:
    max_cnt = cnt_desc
print(max_cnt)
