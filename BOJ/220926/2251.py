def miis(): return map(int,input().split())
def dfs(filled, visited):
    # TW : target에 들어갈 수 있는 물의 양
    # MW : 내가 들고 있는 물의 양
    # TW보다 MW가 적거나 같으면 상관 없음
    # TW보다 MW가 크면 TW만큼만 넣고 MW에서 TW 빼기
    if filled[0] > 0:
        MW = filled[0]
        TW = caps[1]-filled[1] # 0의 물을 1에게 줄거임
        if TW > 0:
            if TW < MW:
                temp = filled[:]
                temp[0] -= TW
                temp[1] += TW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
            else:
                temp = filled[:]
                temp[0] = 0
                temp[1] += MW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
        TW = caps[2]-filled[2] # 0의 물을 2에게 줄거임
        if TW > 0:
            if TW < MW:
                temp = filled[:]
                temp[0] -= TW
                temp[2] += TW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
            else:
                temp = filled[:]
                temp[0] = 0
                temp[2] += MW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
    else:
        rst.add(filled[2])
    if filled[1] > 0:
        MW = filled[1]
        TW = caps[2]-filled[2] # 1의 물을 2에게 줄거임
        if TW > 0:
            if TW < MW:
                temp = filled[:]
                temp[1] -= TW
                temp[2] += TW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
            else:
                temp = filled[:]
                temp[1] = 0
                temp[2] += MW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
        TW = caps[0]-filled[0] # 1의 물을 0에게 줄거임
        if TW > 0:
            if TW < MW:
                temp = filled[:]
                temp[1] -= TW
                temp[0] += TW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
            else:
                temp = filled[:]
                temp[1] = 0
                temp[0] += MW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
    if filled[2] > 0:
        MW = filled[2]
        TW = caps[1]-filled[1] # 2의 물을 1에게 줄거임
        if TW > 0:
            if TW < MW:
                temp = filled[:]
                temp[2] -= TW
                temp[1] += TW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
            else:
                temp = filled[:]
                temp[2] = 0
                temp[1] += MW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
        TW = caps[0]-filled[0] # 2의 물을 0에게 줄거임
        if TW > 0:
            if TW < MW:
                temp = filled[:]
                temp[2] -= TW
                temp[0] += TW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
            else:
                temp = filled[:]
                temp[2] = 0
                temp[0] += MW
                if temp not in visited:
                    visited.append(temp)
                    dfs(temp, visited)
caps = list(miis())
filled = [0, 0, caps[2]+0]
rst = set()
rst.add(caps[2])
dfs(filled, [])
print(*sorted(list(rst)))
