octodict = dict()
cnt = 0
for i in "-\(@?>&%":
    octodict[i] = cnt
    cnt += 1
octodict["/"] = -1
while True:
    target = input()
    if target == "#":
        break
    val = 0
    amp = 1
    for i in target[::-1]:
        val += amp * octodict[i]
        amp *= 8
    print(val)
