# https://www.acmicpc.net/problem/17266
def check_light(lamp, N, height):
    current = 0
    for i in range(len(lamp)):
        left = max(0, lamp[i] - height)  # 0까지만 비출 수 있음
        right = min(N, lamp[i] + height)  # N까지만 비출 수 있음
        if left <= current:
            current = right
        else:
            return False
    return current >= N


def find_height(N, lamp):
    left, right = 0, N

    while left <= right:
        mid = (left + right) // 2
        if check_light(lamp, N, mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


N = int(input())
M = int(input())
lamp = list(map(int, input().split()))

result = find_height(N, lamp)
print(result)