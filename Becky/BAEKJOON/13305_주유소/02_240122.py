# https://www.acmicpc.net/problem/13305
# 18:07-18:26
import sys

N = int(input())
distance = list(map(int, sys.stdin.readline().rstrip().split()))
oil = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0
oil_price = oil[0]
for i in range(N - 1):
    if oil[i] < oil_price:
        oil_price = oil[i]
    ans += distance[i] * oil_price

print(ans)
