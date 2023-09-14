import sys
from collections import deque

input = sys.stdin.readline

dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

def bfs(sz, sy, sx, graph, l, r, c):
    q = deque([(sz, sy, sx)])
    graph[sz][sy][sx] = 0
    while q:
        (z, y, x) = q.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and (graph[nz][ny][nx] == "." or graph[nz][ny][nx] == "E"):
                graph[nz][ny][nx] = graph[z][y][x] + 1
                q.append((nz, ny, nx))
    print(graph)
    return graph
def solution(l, r, c):
    building = []
    dest = [0, 0, 0]

    for _ in range(l):
        floor = [list(input().rstrip()) for _ in range(r)]
        building.append(floor)
        input()
    graph = building
    for z in range(l):
        for y in range(r):
            for x in range(c):
                if building[z][y][x] == "S":
                    graph = bfs(z, y, x, building, l, r, c)
                elif building[z][y][x] == "E":
                    dest = [z, y, x]
    return graph[dest[0]][dest[1]][dest[2]]


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    ans = solution(l, r, c)
    print(ans)
    if ans == "E":
        print("Trapped!")
    else:
        print("Escaped in" + str(ans) + "minute(s).")







