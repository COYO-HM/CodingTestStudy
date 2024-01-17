# https://www.acmicpc.net/problem/2531
# 10:07-10:57
import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().rstrip().split())
sushi = list(int(input().rstrip()) for _ in range(N))

max_len = 0
for i in range(N):
    if i + k > N:
        dishes = len(set(sushi[i:N] + sushi[:(i + k) % N] + [c]))
    else:
        dishes = len(set(sushi[i: i + k] + [c]))
    max_len = max(max_len, dishes)

print(max_len)

# 아래 코드로 하면 sushi[:(i + k) % N] 연산이 오래 걸리는 것 같음
# dishes = len(set(sushi[i: i + k] + sushi[:(i + k) % N] + [c]))
# max_len = max(max_len, dishes)
