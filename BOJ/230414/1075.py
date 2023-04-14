N = int(input())
F = int(input())
N = (N//100)*100
target = N%F
if target == F:
    print('00')
else:
    if target > 0:
        target = F-target
    print('%02d' % target)
