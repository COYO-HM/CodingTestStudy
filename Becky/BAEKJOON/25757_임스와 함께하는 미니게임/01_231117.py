# https://www.acmicpc.net/problem/25757
import sys

N, game = map(str, input().split())

player = set()
for _ in range(int(N)):
    player.add(sys.stdin.readline())

player_number = len(player)
if game == "Y":
    result = player_number
elif game == "F":
    result = player_number // 2
else:
    result = player_number // 3

print(result)
