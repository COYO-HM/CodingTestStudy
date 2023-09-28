# https://www.acmicpc.net/problem/15686
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def combination(chickens, M):
    combinations = []

    def calc(start, current_combi):
        if len(current_combi) == M:
            combinations.append(current_combi[:])
            return

        for i in range(start, len(chickens)):
            current_combi.append(chickens[i])
            calc(i + 1, current_combi)
            current_combi.pop()

    calc(0, [])
    return combinations


def calc_distance(chickens, houses, M):
    chickens_combi = combination(chickens, M)  # 조합 계산
    result = float("inf")

    for chicken in chickens_combi:  # 조합에 맞춰 치킨집과 집 거리 계산하기
        total_distance = 0
        for house in houses:
            distance = float("inf")
            for i in range(M):
                distance = min(distance, abs(house[0] - chicken[i][0]) + abs(house[1] - chicken[i][1]))
            total_distance += distance
        result = min(result, total_distance)

    return result


chickens = []
houses = []
# 치킨집, 가정집 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chickens.append((i, j))
        elif graph[i][j] == 1:
            houses.append((i, j))

print(calc_distance(chickens, houses, M))