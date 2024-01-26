# https://www.acmicpc.net/problem/1515
# 15:09-16:14
import sys

N = sys.stdin.readline().rstrip()
ans = 0

while N:
    ans += 1
    number = str(ans)
    while len(number) and len(N):
        if number[0] == N[0]:
            N = N[1:]
        number = number[1:]

print(ans)
