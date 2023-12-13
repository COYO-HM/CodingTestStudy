# https://www.acmicpc.net/problem/1515
# 00:31(H:M)

import sys
number = sys.stdin.readline().rstrip()
N = 0
while True:
    N += 1
    number_str = str(N)
    while len(number) > 0 and len(number_str) > 0:
        if number[0] == number_str[0]:
            number = number[1:]
        number_str = number_str[1:]

    if number == "":
        print(N)
        break
