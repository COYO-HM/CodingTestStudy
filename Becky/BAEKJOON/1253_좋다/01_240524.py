# https://www.acmicpc.net/problem/1253
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().rstrip().split()))
lst.sort()

cnt = 0
for i in range(N):
    target = lst[i]
    l, r = 0, N - 1

    while l < r:
        s = lst[l] + lst[r]
        if s == target:
            if l == i:
                l += 1
            elif r == i:
                r -= 1
            else:
                cnt += 1
                break
        elif s > target:
            r -= 1
        elif s < target:
            l += 1

print(cnt)
