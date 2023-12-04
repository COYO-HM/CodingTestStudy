# 문제: https://www.acmicpc.net/problem/1244
# loop 탈출 조건 조심
N = int(input())  # 스위치 개수
status = [-1] + list(map(int, input().split()))
students_N = int(input())
students = [list(map(int, input().split())) for _ in range(students_N)]

for student in students:
    gender, idx = student
    if gender == 1:
        for i in range(idx, len(status), idx):
            status[i] = 1 if status[i] == 0 else 0

    else:
        status[idx] = 1 if status[idx] == 0 else 0

        l, r = idx - 1, idx + 1
        while l > 0 and r <= N and status[l] == status[r]:
            if status[l] == 1:
                status[l], status[r] = 0, 0
            else:
                status[l], status[r] = 1, 1
            l -= 1
            r += 1

for i in range(1, N + 1, 20):
    print(*status[i : i + 20])
