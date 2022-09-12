datend = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
N = int(input())
board = []
for _ in range(N):
    line = list(map(int,input().split()))
    # 월 일로 된 데이터를 1년중 몇 번째 일인지 변환하는 과정
    board.append((sum(datend[:line[0]-1]) + line[1],sum(datend[:line[2]-1]) + line[3]))
now_min = 0
now_max = 365
# 제약 : 60 ~ 335
now_min_val = 60
now_max_val = 335
cnt = 0
prev_min = 0
prev_max = 0
while now_min_val < now_max_val:
    # 3.1부터 피어있는 꽃이 없으면 종료
    if len([x for x in board if x[0]<=now_min_val])==0:
        cnt = 0
        break
    # 3.1부터 핀 꽃들 중에 가장 오래까지 피어있는 꽃
    now_min = max([x for x in board if x[0]<=now_min_val],key=lambda x:x[1])
    # 3.1이라는 제약을 현재 꽃이 지는 날짜로 변경
    now_min_val = now_min[1]
    # 꽃 하나 추가
    cnt += 1
    # 이 꽃이 끝까지 다 피었다면 종료(중간점검)
    if now_min_val >= now_max_val:
        break
    # 11.30까지 피어있는 꽃이 없으면 종료
    if len([x for x in board if x[1]>=now_max_val])==0:
        cnt = 0
        break
    # 11.30까지 피어있는 꽃들 중에 가장 먼저 피어있는 꽃
    now_max = min([x for x in board if x[1]>=now_max_val],key=lambda x:x[0])
    # 11.30이라는 제약을 현재 꽃이 피기 시작한 날짜로 변경
    now_max_val = now_max[0]
    # 꽃 하나 추가
    cnt += 1
    # 무한루프 방지용 이스케이프 코드
    if prev_min == now_min_val and prev_max == now_max_val:
        cnt = 0
        break
    prev_min = now_min_val+0
    prev_max = now_max_val+0

print(cnt)
