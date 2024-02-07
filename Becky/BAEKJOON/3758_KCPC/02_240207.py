# https://www.acmicpc.net/problem/3758
# 21:05-21:59
for _ in range(int(input())):
    n, k, t, m = map(int, input().split())  # 팀의 개수, 문제 개수, 팀 ID, 로그 엔트리 개수

    lst = [list(map(int, input().split())) for _ in range(m)]

    score = [[0 for _ in range(k)] for _ in range(n)]  # 점수, 제출 순서
    count_submit = [0] * n
    submit_time = [0] * n

    num = 1
    for l in lst:
        i, j, s = l
        count_submit[i - 1] += 1
        if score[i - 1][j - 1] < s:
            score[i - 1][j - 1] = s
        submit_time[i - 1] = num
        num += 1

    # 팀 ID, 총합, 제출 순서, 제출 횟수
    total_score = [[i, 0, submit_time[i - 1], count_submit[i - 1]] for i in range(1, n + 1)]
    for i in range(len(score)):
        for j in range(len(score[0])):
            total_score[i][1] += score[i][j]

    total_score.sort(key=lambda x: (-x[1], x[3], x[2]))

    for i in range(1, n + 1):
        if total_score[i - 1][0] == t:
            print(i)