# https://www.acmicpc.net/problem/11501
# 19:52-20:41
import sys
for _ in range(int(input())):
    N = int(input())
    stock = list(map(int, sys.stdin.readline().split()))

    profit = 0
    max_val = 0

    for i in range(N - 1, -1, -1):
        if stock[i] > max_val:
            max_val = stock[i]
        else:
            profit += max_val - stock[i]

    print(profit)