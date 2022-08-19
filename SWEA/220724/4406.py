T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
aeiou = 'aeiou'
for test_case in range(1, T + 1):
    word = input()
    print(f'#{test_case} ',end='')
    for i in word:
        if i not in aeiou:
            print(i,end='')
    print()
