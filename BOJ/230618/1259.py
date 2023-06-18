while True:
    target = input()
    if target == "0":
        break
    if target == target[::-1]:
        print("yes")
    else:
        print("no")
