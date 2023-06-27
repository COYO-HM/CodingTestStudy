# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    days = [0 for _ in range(len(progresses))]
    for i in range(len(progresses)):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            days[i] += 1

    answer = []
    val = days[0] # 처음 값으로 초기화
    cnt = 0
    for i in range(len(days)):
        if val >= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            val = days[i]
            cnt = 1

    answer.append(cnt) # 마지막 배포

    return answer