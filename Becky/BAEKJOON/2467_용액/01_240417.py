# https://www.acmicpc.net/problem/2467
# 21:48-22:29
import sys
N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
l, r = 0, N - 1
x, y = lst[0], lst[-1]
s = x + y

while l < r:
    x_val, y_val = lst[l], lst[r]
    tmp = x_val + y_val

    if tmp == 0:
        x, y = x_val, y_val
        break

    if abs(tmp) < abs(s):
        x, y = x_val, y_val
        s = tmp
    else:
        if tmp < 0:
            l += 1
        else:
            r -= 1

print(x, y)
