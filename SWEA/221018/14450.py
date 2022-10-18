def miis(): return map(int,input().split())
def ii(): return int(input())
T = ii()
for tc in range(1, T+1):
    L, R, Q = input().split()
    line = input().split()
    ans = f'#{tc} '
    for i in line:
        targetlen = len(i)
        if len(R) < targetlen:
            ans += 'X'
        elif len(L) == len(R):
            if int(L[:targetlen]) <= int(i) <= int(R[:targetlen]):
                ans += 'O'
            else:
                ans += 'X'
        elif len(R)-len(L) == 1:
            if targetlen <= len(L):
                for j in range(len(L)-targetlen-1, len(R)+1):
                    if int(L) <= int(i+'0'*j) <= int(R):
                        ans += 'O'
                        break
                    if int(L) <= int(i+'9'*j) <= int(R):
                        ans += 'O'
                        break
                else:
                    ans += 'X'
            elif int(i) <= int(R):
                ans += 'O'
            else:
                ans += 'X'
        else:
            if len(L) < targetlen < len(R):
                ans += 'O'
            elif int(L) <= int(i) <= int(R):
                ans += 'O'
            else:
                for j in range(len(L)-targetlen-1, len(R)+1):
                    if int(L) <= int(i+'0'*j) <= int(R):
                        ans += 'O'
                        break
                    if int(L) <= int(i+'9'*j) <= int(R):
                        ans += 'O'
                        break
                else:
                    ans += 'X'
    print(ans)

