# https://www.acmicpc.net/problem/20437
# 16:05-16:27
strings = list('abcdefghijklmnopqrstuvwxyz')
for _ in range(int(input())):
    w = list(input())
    k = int(input())

    min_len, max_len = len(w) + 1, 0
    for s in strings:
        idx = []
        if w.count(s) >= k:
            for i in range(len(w)):
                if w[i] == s:
                    idx.append(i)
        else:
            continue

        for i in range(len(idx) - k + 1):
            result = idx[i + k - 1] - idx[i] + 1
            min_len = min(min_len, result)
            max_len = max(max_len, result)

    if min_len == len(w) + 1:
        print(-1)
    else:
        print(min_len, max_len)
