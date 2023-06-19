aeiou = "aeiouAEOIU"
while True:
    cnt = 0
    target = input()
    if target == "#":
        break
    for i in target:
        if i in aeiou:
            cnt += 1
    print(cnt)
