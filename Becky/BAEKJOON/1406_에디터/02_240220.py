# https://www.acmicpc.net/problem/1406
# 16:20-32
import sys

input = sys.stdin.readline
l_stack, r_stack = list(input().rstrip()), []

for _ in range(int(input().rstrip())):
    order = input().rstrip()

    if order[0] == "L":
        if l_stack:
            p = l_stack.pop()
            r_stack.append(p)
    elif order[0] == "D":
        if r_stack:
            p = r_stack.pop()
            l_stack.append(p)
    elif order[0] == "B":
        if l_stack:
            l_stack.pop()
    else:
        P, s = order.split()
        l_stack.append(s)

r_stack = r_stack[::-1]
print("".join(l_stack + r_stack))
