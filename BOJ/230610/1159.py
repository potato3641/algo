from collections import defaultdict
N = int(input())
mydict = defaultdict(int)
for i in range(N):
    mydict[input()[0]] += 1
answer = []
for i in mydict:
    if mydict[i] >= 5:
        answer.append(i)
if answer:
    print(*sorted(answer), sep='')
else:
    print("PREDAJA")
