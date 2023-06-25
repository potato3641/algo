name, N = input(), int(input())
line = tuple(input() for _ in range(N))
target = "LOVE"
L, O, V, E = name.count("L"), name.count("O"), name.count("V"), name.count("E")
maxper = 0
maxname = "ZZZZZZZZZZZZZZZZZZZZ"
for teams in line:
    l, o, v, e = L+teams.count("L"), O+teams.count("O"), V+teams.count("V"), E+teams.count("E")
    per = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100
    if maxper < per:
        maxper = per
        maxname = teams
    elif maxper == per:
        for i in range(min(len(maxname), len(teams))):
            if maxname[i] < teams[i]:
                break
            elif maxname[i] == teams[i]:
                continue
            else:
                maxname = teams
                break
        else:
            if maxname > teams:
                maxname = teams
print(maxname)
