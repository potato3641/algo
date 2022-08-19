# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    rst = []
    cse90 = []
    cse180 = []
    cse270 = []
    for i in range(0,N):
        arr.append(list(map(int,input().split())))
    for j in range(N):
        line = []
        for i in range(N):
            line.append(arr[N-1-i][j])
        cse90.append(line)
    for j in range(N):
        line = []
        for i in range(N):
            line.append(cse90[N-1-i][j])
        cse180.append(line)
    for j in range(N):
        line = []
        for i in range(N):
            line.append(cse180[N-1-i][j])
        cse270.append(line)
    print('#{}'.format(test_case))
    for i in range(N):
        print(''.join(map(str,cse90[i])), end='')
        print(' ', end='')
        print(''.join(map(str,cse180[i])), end='')
        print(' ', end='')
        print(''.join(map(str,cse270[i])))

