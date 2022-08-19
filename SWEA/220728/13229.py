T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
wd = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
for test_case in range(1, T + 1):
    S = input()
    print(f'#{test_case} {6 - wd.index(S) if 6 != wd.index(S) else 7}')
