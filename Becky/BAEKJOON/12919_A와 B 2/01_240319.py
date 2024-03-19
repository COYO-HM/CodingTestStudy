# https://www.acmicpc.net/problem/12919
# 16:40-17:16
S = list(input())
T = list(input())


def check(T):
    if T == S:
        return 1

    if len(T) == 0:
        return 0

    if T[-1] == 'A':
        if check(T[:-1]):
            return 1
    if T[0] == 'B':
        if check(T[1:][::-1]):
            return 1
    return 0

print(1) if check(T) else print(0)
