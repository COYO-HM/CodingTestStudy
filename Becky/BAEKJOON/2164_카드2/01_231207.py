# https://www.acmicpc.net/problem/2164
# 시작: 2:20
# 종료: 2:25
from collections import deque

N = int(input())
cards = deque([i for i in range(1, N + 1)])

while len(cards) != 1:
    cards.popleft()
    card = cards.popleft()
    cards.append(card)

print(*cards)
