# https://www.acmicpc.net/problem/23971
import math
H, W, N, M = map(int, input().split())
r = math.ceil(H / (N + 1))
c = math.ceil(W / (M + 1))

result = r * c
print(result)