T = int(input())
for tc in range(1, T + 1):
    max_fuel, len_stops, cnt_lines = map(int,input().split())
    line = list(map(int,input().split())) + [len_stops]
    prev = 0
    fuel = max_fuel
    rst = 0
    for i in range(cnt_lines):
        fuel -= line[i] - prev
        if fuel < 0:
            rst = 0
            break
        prev = line[i]
        if line[i+1] - prev > fuel or fuel == 0:
            rst += 1
            fuel = max_fuel
    print(f'#{tc} {rst}')
        
        
