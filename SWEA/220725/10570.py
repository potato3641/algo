T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B = map(int,input().split())
    rst = 0
    for i in range(A,B+1):
        if str(i) == str(i)[::-1]:
            if str(i**(1/2))[-2:]=='.0':
            	if str(int(i**(1/2))) == str(int(i**(1/2)))[::-1]:
	                rst += 1
    print(f'#{test_case} {rst}')
