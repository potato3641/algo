from collections import defaultdict
def solution(s):
    tempDict = defaultdict(int)
    cnt = 1
    temp = []
    for i in s:
        if tempDict[i] == 0:
            temp.append(-1)
        else:
            temp.append(cnt-tempDict[i])
        tempDict[i] = cnt
        cnt += 1
    return temp
