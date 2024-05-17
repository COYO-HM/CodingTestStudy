# https://www.acmicpc.net/problem/22251
N, K, P, X = map(int, input().split())  # 최대 층수, 자리수, 최대 반전 가능 개수, 현재 층

numbers = {
    "0": [1, 1, 1, 0, 1, 1, 1], "1": [0, 0, 1, 0, 0, 1, 0],
    "2": [1, 0, 1, 1, 1, 0, 1], "3": [1, 0, 1, 1, 0, 1, 1],
    "4": [0, 1, 1, 1, 0, 1, 0], "5": [1, 1, 0, 1, 0, 1, 1],
    "6": [1, 1, 0, 1, 1, 1, 1], "7": [1, 0, 1, 0, 0, 1, 0],
    "8": [1, 1, 1, 1, 1, 1, 1], "9": [1, 1, 1, 1, 0, 1, 1]
}

led_cost = {}
for i in range(10):
    for j in range(10):
        cost = sum(1 for x, y in zip(numbers[str(i)], numbers[str(j)]) if x != y)
        led_cost[(i, j)] = cost


def check_valid(n, k, p, x):
    # 현재 층수 X를 문자열로 변환하고, 자리수를 맞추기 위해 0으로 채움
    current_floor = str(x).zfill(k)
    cnt = 0

    for i in range(1, n + 1):
        target_floor = str(i).zfill(k)
        total_changes = sum(led_cost[(int(cf), int(tf))] for cf, tf in zip(current_floor, target_floor))
        if 1 <= total_changes <= p:
            cnt += 1

    return cnt


print(check_valid(N, K, P, X))
