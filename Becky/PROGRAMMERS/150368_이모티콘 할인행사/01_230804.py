# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 1. 이모티콘 플러스 서비스 가입자를 최대한 늘리고
# 2. 이모티콘 판매액을 최대한 늘리는 것
# 이 조건을 어떻게 구현할 지 모르겠음
from itertools import product


def solution(users, emoticons):
    discount_rates = [0.9, 0.8, 0.7, 0.6]
    arr = [[int(emoticon * rate) for rate in discount_rates] for emoticon in emoticons]
    # for a in arr:
    #     print(a)

    # users percent를 범위로 수정
    for idx, val in enumerate(users):
        if users[idx][0] > 30:  # 40%이상 할인 하면 구입
            users[idx][0] = 3
        elif users[idx][0] > 20:  # 30%이상 할인 하면 구입
            users[idx][0] = 2
        elif users[idx][0] > 10:  # 20%이상 할인 하면 구입
            users[idx][0] = 1
        else:  # 10%이상 할인 하면 구입
            users[idx][0] = 0

    l_emogi = len(emoticons)
    products = list(product([0, 1, 2, 3], repeat=l_emogi))  # 중복 순열

    result = []
    for p in products:
        plus_member = 0
        for i in range(l_emogi):
            revenue = 0
            for idx, cost in users:
                if idx >= p[i]:
                    revenue += arr[i][p[i]]
                if revenue >= cost:
                    plus_member += 1
                    revenue = 0
                    continue
        result.append([plus_member, revenue])
    # print(result)
    answer = []
    return answer
