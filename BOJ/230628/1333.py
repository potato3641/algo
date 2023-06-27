N, L, D = map(int,input().split())
song = False
songstart = 0
answer = 0
for timer in range(N*L*D+1):
    if not song and timer >= songstart and N:
        songstart += L
        song = True
        N -= 1
        continue
    if songstart == timer:
        songstart += 5
        song = False
    if not song and timer%D == 0:
        answer = timer
        break
print(answer)
