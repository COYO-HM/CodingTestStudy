# https://www.acmicpc.net/problem/9017
# 푸는데 정말 오래 걸렸다. 중첩 if문을 안 쓰는 방법으로 하려다가 망함
# 인덱스가 명확하지 않고, 리스트 안에 팀 번호가 있어서 코드 가독성이 별로
# 인덱스 신경 써서 다시 풀어볼 것

import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    athletes = list(map(int, input().strip().split()))
    M = max(athletes)
    team = list([i, 0, 0, 0] for i in range(1, M + 1))
    out = []

    for i in range(1, M + 1):
        if athletes.count(i) < 6:  # 6명 미만 출전 경우 점수 X
            team[i - 1][1] = -1
            out.append(i - 1)

    score = 1
    for a in athletes:
        a -= 1
        if a not in out:
            if team[a][2] < 4:
                team[a][1] += score
                team[a][2] += 1
            elif team[a][2] == 4:
                team[a][3] = score
                team[a][2] += 1
            score += 1

    team.sort(key=lambda x: (x[1], x[3]))
    for t in team:
        if t[1] != -1:
            print(t[0])
            break
