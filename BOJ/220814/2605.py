N = int(input())
line = list(map(int,input().split()))
student = []
cnt = 1
for i in line:
    if i:
        student.append(cnt)
        student[-1-i:] = [student[-1]] + student[-1-i:-1]
    else:
        student.append(cnt)
    cnt += 1
print(*student)
