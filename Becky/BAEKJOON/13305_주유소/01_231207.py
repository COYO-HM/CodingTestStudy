# https://www.acmicpc.net/problem/13305
# 시작: 14:32
# 종료: 14:52
N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
p = price[0]
for i in range(N - 1):
    if price[i] < p:  # 싼 기름을 넣기
        p = price[i]
    result += p * distance[i]

print(result)
