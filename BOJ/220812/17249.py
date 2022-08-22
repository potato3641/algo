get_char = input()
left_punch_cnt = 0
right_punch_cnt = 0
face_flag = False
for i in get_char:
    if ord(i) == 64 and not face_flag:
        left_punch_cnt += 1
    if ord(i) == 48:
        face_flag = True
    if ord(i) == 64 and face_flag:
        right_punch_cnt += 1
print(left_punch_cnt, right_punch_cnt)
