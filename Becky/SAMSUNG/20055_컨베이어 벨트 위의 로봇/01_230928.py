# https://www.acmicpc.net/problem/20055
# PyPy3으로 제출해야 통과 => deque 사용해서 다시 풀기
N, K = map(int, input().split())
lst = list(map(int, input().split()))
belt = [[i, 0] for i in lst]  # (내구도, 로봇 여부)
l = len(belt)
cnt = 0

while True:
    # 1. 회전
    belt = [belt[-1]] + belt[:-1]

    # 내리는 위치 도달시 즉시 내림
    belt[N - 1][1] = 0

    #  2. 벨트가 회전하는 방향으로 한 칸 이동할 수 있으면 로봇 이동
    for i in range(N - 2, -1, -1):
        if belt[i][1] == 1:
            if (belt[i + 1][1] == 0) and (belt[i + 1][0] > 0):
                belt[i][1] = 0  # 기존 위치에 있던 로봇 옮기기
                belt[i + 1][1] = 1  # 로봇 이동
                belt[i + 1][0] -= 1  # 내구도 감소

    # 내리는 위치 도달시 즉시 내림
    belt[N - 1][1] = 0

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇 올리기
    if belt[0][0] > 0:
        belt[0][1] = 1  # 로봇 올리기
        belt[0][0] -= 1  # 내구도 감소

    cnt += 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상인 경우 종료
    count_0 = 0
    for i in range(l):
        if belt[i][0] == 0:
            count_0 += 1
    if count_0 >= K:
        break

print(cnt)