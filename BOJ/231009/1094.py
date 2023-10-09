N = int(input())
mark = [64]
while sum(mark) > N:
    target = min(mark)
    mark.remove(target)
    target1 = target // 2
    target2 = target - target1
    smark = sum(mark)
    if smark+target1 >= N:
        mark.append(target2)
    elif smark+target2 >= N:
        mark.append(target1)
    else:
        mark.append(target1)
        mark.append(target2)
print(len(mark))
