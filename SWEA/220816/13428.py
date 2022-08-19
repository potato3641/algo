def minwithoutyou(line, targets):
    min_num = 10
    flag1 = False
    for i in line:
        if i < min_num and i not in targets:
            min_num = i
            flag1 = True
    if flag1:
        return min_num
    else:
        return 0
T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int,list(input())))
    min_nums, max_nums = nums[:], nums[:]
    for i in range(len(nums)):
        min_num = min(nums[i:])
        if not i and not min_num:
            min_num = minwithoutyou(nums[i:],[0])
        min_num_idx = nums.index(min_num)
        if min_nums[i] != min_nums[min_num_idx]:
            if not i+min_num:
                continue
            else:
                min_num_idx_back = len(nums)-nums[::-1].index(min_num)-1
                min_nums[i], min_nums[min_num_idx_back] = \
                min_nums[min_num_idx_back], min_nums[i]
            break
    for i in range(len(nums)):
        max_num = max(nums[i:])
        max_num_idx = nums.index(max_num)
        if max_nums[i] != max_nums[max_num_idx]:
            max_num_idx_back = len(nums)-nums[::-1].index(max_num)-1
            max_nums[i], max_nums[max_num_idx_back] = \
            max_nums[max_num_idx_back], max_nums[i]
            break
    print(f'#{tc}', ''.join(map(str,min_nums)), ''.join(map(str,max_nums)))
