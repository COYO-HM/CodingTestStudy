# https://www.acmicpc.net/problem/7682
# 복붙 주의(인덱스 번호 틀려서 틀림)
while (True):
    tc = input()
    if tc == "end":
        break

    x_cnt, o_cnt, etc_cnt = tc.count("X"), tc.count("O"), tc.count(".")
    if o_cnt > x_cnt or abs(x_cnt - o_cnt) > 1 or x_cnt < 3:
        print("invalid")
        continue

    o_check, x_check = 0, 0
    for i in range(0, 9, 3):
        tmp = tc[i]
        if tmp == tc[i + 1] == tc[i + 2]:
            if tmp == "O":
                o_check += 1
            elif tmp == "X":
                x_check += 1

    for i in range(3):
        tmp = tc[i]
        if tmp == tc[i + 3] == tc[i + 6]:
            if tmp == "O":
                o_check += 1
            elif tmp == "X":
                x_check += 1

    if tc[0] == tc[4] == tc[8]:
        tmp = tc[0]
        if tmp == "O":
            o_check += 1
        elif tmp == "X":
            x_check += 1

    if tc[2] == tc[4] == tc[6]:
        tmp = tc[2]
        if tmp == "O":
            o_check += 1
        elif tmp == "X":
            x_check += 1

    # x가 o보다 많은 경우 => x가 승리
    # o와 x의 개수가 같은 경우 => o가 승리
    # 동시에 승리 불가능

    if x_cnt > o_cnt:
        if o_check:
            print("invalid")
            continue
    elif x_cnt == o_cnt:
        if x_check:
            print("invalid")
            continue

    if x_check and o_check:
        print("invalid")
        continue

    if etc_cnt > 0:
        if not x_check and not o_check:
            print("invalid")
            continue
    print("valid")
