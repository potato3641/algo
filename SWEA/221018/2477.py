from collections import deque
def sims(t, w1, w2, cnt):
    # 정비 창구 처리
    for i in range(M):
        if jungb[i] == 0:
            continue
        if jungb[i] == jb[i]:
            jungb[i] = 0
        else:
            jungb[i] += 1
    # w2 처리
    if w2 and jungb.count(0):
        for i in range(M):
            if jungb[i]==0:
                jungb[i] = 1
                target, target_val = w2.popleft()
                visited[target] = (target_val, i)
                if len(w2) < 1 or jungb.count(0)==0:
                    break
    # 접수 창구 처리
    for i in range(N):
        if jubs[i] == 0:
            continue
        if jubs[i] == js[i]:
            jubs[i] = 0
            if len(visited)==0:
                break
            if jungb.count(0):
                for j in range(M):
                    if jungb[j]==0:
                        jungb[j] = 1
                        visited[[x for x in visited if visited[x]==i][0]] = (i, j)
                        break
            else:
                target = [x for x in visited if visited[x]==i]
                if len(target):
                    target = target[0]
                    w2.append((target, visited[target]))
                    del visited[target]
        else:
            jubs[i] += 1
    # w1 처리
    if w1 and jubs.count(0):
        for i in range(N):
            if jubs[i]==0:
                jubs[i] = 1
                visited[w1.popleft()] = i
                if len(w1) < 1 or jubs.count(0)==0:
                    break
    # 고객 입장
    if max(customer) < t and jubs.count(0)==N and len(w1)==0 and len(w2)==0:
        return 
    for _ in range(customer.count(t)):
        cnt += 1
        if jubs.count(0):
            for i in range(N):
                if jubs[i]==0:
                    jubs[i] = 1
                    visited[cnt] = i
                    break
        else:
            w1.append(cnt)
    return sims(t+1, w1, w2, cnt)
T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int,input().split())
    js = list(map(int,input().split()))
    jb = list(map(int,input().split()))
    customer = list(map(int,input().split()))
    visited = dict()
    jubs = [0]*N
    jungb = [0]*M
    sims(0, deque(), deque(), 0)
    ans = 0
    for k in visited:
        if visited[k] == (A-1, B-1):
            ans += k
    if ans:
        print(f'#{tc}', ans)
    else:
        print(f'#{tc}', -1)
