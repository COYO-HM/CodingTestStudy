# https://www.acmicpc.net/problem/3758
# 11:27 - 12:20
for tc in range(int(input())):
    n, k, my_team, m = map(int, input().split())  # 팀 개수, 문제 개수, 내 팀 ID, 로그 엔트리
    score_list = [[0 for _ in range(k)] for _ in range(n)]  # 점수 리스트
    check = {i: [0, 0] for i in range(n)}  # 시도 횟수, 제출 순위
    solved = [list(map(int, input().split())) for _ in range(m)]

    for idx, (id_num, problem_num, score) in enumerate(solved):
        score_list[id_num - 1][problem_num - 1] = max(score, score_list[id_num - 1][problem_num - 1])
        check[id_num - 1][0] += 1
        check[id_num - 1][1] = idx

    total = {key: sum(s) for key, s in enumerate(score_list)}

    ranking = {key: (check[key] + [total.get(key, 0)]) for key in check}

    # 랭킹 계산
    ranking = sorted(ranking.items(), key=lambda x: (x[1][2], -x[1][0], -x[1][1]), reverse=True)
    answer = [team[0] for team in ranking].index(my_team - 1) + 1

    print(answer)
