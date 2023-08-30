import sys
input = sys.stdin.readline
n = int(input())
chart = [map(int, input().split()) for _ in range(n)]
dp = [0] * n
for i, [t, p] in enumerate(chart):


