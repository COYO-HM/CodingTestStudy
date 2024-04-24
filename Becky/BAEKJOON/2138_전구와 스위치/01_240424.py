# https://www.acmicpc.net/problem/2138
# 20:55-21:32
N = int(input())
curr = list(map(int, input()))
target = list(map(int, input()))


def change(A, B):
    A_copy = A[:]
    cnt = 0

    for i in range(1, N):
        if A_copy[i - 1] == B[i - 1]:
            continue

        cnt += 1
        for j in range(i - 1, i + 2):
            if j < N:
                A_copy[j] = 1 - A_copy[j]

    if A_copy == B:
        return cnt
    else:
        return 1e9


ans = change(curr, target)

curr[0] = 1 - curr[0]
curr[1] = 1 - curr[1]

ans = min(ans, change(curr, target) + 1)

print(ans) if ans != 1e9 else print(-1)
