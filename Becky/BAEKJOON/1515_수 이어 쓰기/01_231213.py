# https://www.acmicpc.net/problem/1515
# 00:31(H:M)

import sys
input = sys.stdin.readline().rstrip()
ans = 0
while True:
    ans += 1
    number = str(ans)
    while len(input) > 0 and len(number) > 0:
        if input[0] == number[0]:
            input = input[1:]
        number = number[1:]

    if input == "":
        print(ans)
        break
