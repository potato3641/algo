T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    line = input()
    word = []
    rst = 0
    flag = False
    for i in line:
        word.append(i)
        rst = len(word)
        dummy = line[rst:]
        if (dummy[:rst] == ''.join(word)) & (set(''.join(word)) == set(dummy[-rst:])):
            flag = True
            break
        if flag:
            break
    print(f'#{test_case} {rst}')
