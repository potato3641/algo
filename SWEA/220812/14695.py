T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    points = [[] for _ in range(N)]
    vecAXIS = []
    rst = 1
    for i in range(N):
        points[i] = list(map(int,input().split()))
        if i == 2:
            vecAXIS = [(points[1][1]-points[0][1])*(points[1][2]-points[i][2])-(points[1][2]-points[0][2])*(points[1][1]-points[i][1]), \
                       (points[1][0]-points[0][0])*(points[1][2]-points[i][2])-(points[1][2]-points[0][2])*(points[1][0]-points[i][0]), \
                       (points[1][0]-points[0][0])*(points[1][1]-points[i][1])-(points[1][1]-points[0][1])*(points[1][0]-points[i][0])]
        elif i > 2:
            if vecAXIS == [0, 0, 0]:
                vecAXIS = [(points[1][1]-points[0][1])*(points[1][2]-points[i][2])-(points[1][2]-points[0][2])*(points[1][1]-points[i][1]), \
                           (points[1][0]-points[0][0])*(points[1][2]-points[i][2])-(points[1][2]-points[0][2])*(points[1][0]-points[i][0]), \
                           (points[1][0]-points[0][0])*(points[1][1]-points[i][1])-(points[1][1]-points[0][1])*(points[1][0]-points[i][0])]
            vecNOW = [(points[1][1]-points[0][1])*(points[1][2]-points[i][2])-(points[1][2]-points[0][2])*(points[1][1]-points[i][1]), \
                      (points[1][0]-points[0][0])*(points[1][2]-points[i][2])-(points[1][2]-points[0][2])*(points[1][0]-points[i][0]), \
                      (points[1][0]-points[0][0])*(points[1][1]-points[i][1])-(points[1][1]-points[0][1])*(points[1][0]-points[i][0])]
            if vecAXIS[1]*vecNOW[2]-vecAXIS[2]*vecNOW[1] or vecAXIS[0]*vecNOW[1]-vecAXIS[1]*vecNOW[0] or vecAXIS[2]*vecNOW[0]-vecAXIS[0]*vecNOW[2]:
                rst *= 0
    if rst:
        print(f'#{test_case} TAK')
    else:
        print(f'#{test_case} NIE')
