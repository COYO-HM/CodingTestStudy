# 문제: https://www.acmicpc.net/problem/2193
n = int(input())
result = [0] * 91
result[1] = 1
result[2] = 1

for i in range(3, n+1):
    result[i] = result[i-2] + result[i-1]

print(result[n])
