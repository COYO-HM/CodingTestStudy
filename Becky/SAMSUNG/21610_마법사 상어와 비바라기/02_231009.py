# https://www.acmicpc.net/problem/21610
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

direction = ["empty", [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
diagonal = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
clouds = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]  # 초기 구름 좌표
new_clouds = []

for d, s in moves:
    moved_clouds = []
    for r, c in clouds:
        nr = (r + direction[d][0] * s) % N
        nc = (c + direction[d][1] * s) % N
        graph[nr][nc] += 1
        moved_clouds.append([nr, nc])

    # 2. 물복사버그
    # 대각선 방향에 물이 있는 칸 수만큼 graph[r][c] 물의 양 증가
    for r, c in moved_clouds:
        for nr, nc in diagonal:
            dr = r + nr
            dc = c + nc
            if 0 <= dr < N and 0 <= dc < N and graph[dr][dc] > 0:
                graph[r][c] += 1

    # 비구름 생성
    visited = [[0] * N for _ in range(N)]
    for i, j in moved_clouds:
        visited[i][j] = 1

    new_clouds = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] >= 2:
                graph[i][j] -= 2
                new_clouds.append([i, j])
    clouds = new_clouds

# 결과 계산
answer = 0
for r in range(N):
    for c in range(N):
        answer += graph[r][c]
print(answer)
