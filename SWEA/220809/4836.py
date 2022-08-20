def drawing(book, x1, y1, x2, y2, clr):
    adder = 1000
    if clr == 2:
        adder = 1
    for x in range(x1, x2+1):
        book[x] = [book[x][i]+adder if y1 <= i <= y2 else book[x][i] for i in range(len(book[x]))]
    return book
T = int(input())
for test_case in range(1, T + 1):
    color_cnt = int(input())
    color_book = [[0]*10 for i in range(10)]
    rst = 0
    for i in range(color_cnt):
        x1, y1, x2, y2, clr = map(int,input().split())
        color_book = drawing(color_book,x1,y1,x2,y2,clr)
    for i in range(10):
        for j in range(10):
            if color_book[i][j]%10 and color_book[i][j]//10:
                rst += 1
    print(f'#{test_case} {rst}')
        
