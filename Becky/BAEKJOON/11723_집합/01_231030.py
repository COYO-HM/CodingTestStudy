# https://www.acmicpc.net/problem/11723
import sys
S = set()
for _ in range(int(input())):
    order = sys.stdin.readline().strip().split()

    if len(order) == 1:
        if order[0] == "all":
            S = set(i for i in range(1, 21))
        else:
            S = set()

    else:
        f, element = order[0], order[1]
        element = int(element)

        if f == "add":
            S.add(element)
        elif f == "remove":
            S.discard(element)
        elif f == "check":
            print("1") if element in S else print("0")
        elif f == "toggle":
            S.discard(element) if element in S else S.add(element)
