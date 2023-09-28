# https://www.acmicpc.net/problem/15686
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def combination(lst, M):
    combi_lst = []

    def calc_combi(start, current_combi):
        if len(current_combi) == M:
            combi_lst.append(current_combi[:])
            return

        for i in range(start, len(lst)):
            current_combi.append(lst[i])
            calc_combi(i + 1, current_combi)
            current_combi.pop()

    calc_combi(0, [])
    return combi_lst


def calc_distance(chickens, houses, M):
    chickens_combi = combination(chickens, M)
    result = float("inf")

    for chicken in chickens_combi:
        total_distance = 0
        for house in houses:
            distance = float("inf")
            for i in range(M):
                distance = min(distance, abs(chicken[i][0] - house[0]) + abs(chicken[i][1] - house[1]))
            total_distance += distance
        result = min(result, total_distance)

    return result


chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
           chickens.append((i, j))
        elif graph[i][j] == 1:
            houses.append((i, j))

print(calc_distance(chickens, houses, M))