# https://www.acmicpc.net/problem/2304
# 14:15-15:22
# 접근 방식은 맞지만 구현이 너무 오래 걸림
import sys
N = int(input())
storage = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
storage.sort()

max_w, max_h = max(storage, key=lambda x: x[1])


def calc(lst):
    result = 0
    prev_w, prev_h = lst[0]

    for w, h in lst[1:]:
        if w == max_w:
            result += abs(w - prev_w) * prev_h
            return result
        if h > prev_h:
            result += abs(w - prev_w) * prev_h
            prev_w, prev_h = w, h

    return result


if N == 1:
    print(max_h)
else:
    left = calc(storage)
    right = calc(list(reversed(storage)))
    print(left + right + max_h)