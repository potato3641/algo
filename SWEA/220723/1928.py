T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
for test_case in range(1, T + 1):
    ecdstr = input()
    print(f'#{test_case}',end=' ')
    for i in range(len(ecdstr)//4):
        line = ecdstr[i*4:i*4+4]
        bitline = 1
        for i in range(4):
            bitline <<= 6
            bitline += base64.index(line[i])
        print(chr((bitline>>16) & 255),end='')
        print(chr((bitline>>8) & 255),end='')
        print(chr(bitline & 255),end='')
    print()
        
