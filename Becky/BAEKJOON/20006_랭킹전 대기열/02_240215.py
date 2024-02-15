# https://www.acmicpc.net/problem/20006
# 14:03-14:22
import sys

p, m = map(int, input().split())
players = list(sys.stdin.readline().rstrip().split() for _ in range(p))

rooms = [[players[0]]]
players = players[1:]

for l, n in players:
    checkIn = False
    for room in rooms:
        if int(room[0][0]) - 10 <= int(l) <= int(room[0][0]) + 10 and len(room) < m:
            room.append([l, n])
            checkIn = True
            break
    if not checkIn:
        rooms.append([[l, n]])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort(key=lambda x: x[1])
    for r in room:
        print(" ".join(r))
