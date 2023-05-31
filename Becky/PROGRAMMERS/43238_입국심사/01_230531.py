# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    answer = 0

    l, r = 1, max(times) * n
    while l <= r:
        mid = (l + r) // 2
        people = 0
        for time in times:
            people += mid // time

            if people >= n:
                break

        if people >= n:
            answer = mid
            r = mid - 1
        elif people < n:
            l = mid + 1

    return answer