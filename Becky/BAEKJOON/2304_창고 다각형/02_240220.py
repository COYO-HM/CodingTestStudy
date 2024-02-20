# https://www.acmicpc.net/problem/2304
# 16:36-16:52
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


N = int(input())
storage = list(list(map(int, input().split())) for _ in range(N))
storage.sort()

max_w, max_h = max(storage, key=lambda x: x[1])

if N == 1:
    print(max_h)
else:
    l = calc(storage)
    r = calc(list(reversed(storage)))
    print(l + r + max_h)
