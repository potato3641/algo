while True:
    target = input()
    if target == "0":
        break
    N, *line = map(int,target.split())
    val = 1
    for i in range(N):
        val *= line[i*2]
        val -= line[i*2+1]
    print(val)
