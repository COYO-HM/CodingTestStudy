# https://www.acmicpc.net/problem/11501
# 14:52-15:14
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input().rstrip())
    stock = list(map(int, input().rstrip().split()))

    ans = 0
    max_val = 0

    for i in range(N - 1, -1, -1):
        if stock[i] > max_val:
            max_val = stock[i]
        else:
            ans += max_val - stock[i]

    print(ans)