#import sys
#sys.stdin = open("input.txt", "r")
#T = int(input())
a, b = input().split()
a = int(a)
b = int(b)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1):
    # ///////////////////////////////////////////////////////////////////////////////////
    f = ""
    if ( b == (a + 1) ):
        f = "B"
    else:
        if ( b == (a - 2) ):
            f = "B"
        else:
            f = "A"
    print(f)
    # ///////////////////////////////////////////////////////////////////////////////////