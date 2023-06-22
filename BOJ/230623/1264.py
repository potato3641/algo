nums = (4, 2, 3, 3, 3, 3, 3, 3, 3, 3)
while True:
    target = input()
    answer = len(target)+1
    if not int(target):
        break
    for i in target:
        answer += nums[int(i)]
    print(answer)
