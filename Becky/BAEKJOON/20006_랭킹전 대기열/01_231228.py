# https://www.acmicpc.net/problem/20006
# 17:26-18:02
import sys
p, m = map(int, input().split())
rooms = []
for _ in range(p):
    level, name = sys.stdin.readline().rstrip().split()
    level = int(level)

    if not rooms:
        rooms.append([[level, name]])
        continue

    else:
        check = False
        for room in rooms:
            if len(room) < m:
                user_level = int(room[0][0])
                min_bound, max_bound = user_level - 10, user_level + 10

                if min_bound <= level and level <= max_bound:
                    room.append([level, name])
                    check = True
                    break

        if not check:
            rooms.append([[level, name]])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    room.sort(key=lambda x: x[1])
    for level, name in room:
        print(level, name)