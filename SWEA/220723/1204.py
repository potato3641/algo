T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input()
    student = dict()
    line = list(map(int,input().split()))
    line[0] = 0
    max_idx = 0
    for i in line:
        if i in student.keys():
            student[i] += 1
        else:
            student[i] = 1
        if student[max_idx] <= student[i]:
            max_idx = i
    print(f'#{test_case} {max_idx}')
