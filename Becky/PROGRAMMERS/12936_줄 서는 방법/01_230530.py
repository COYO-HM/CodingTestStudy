# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12936
import math

def solution(n, k):
    lst = [i for i in range(1, n + 1)]
    answer = []

    while (n != 0):
        num = factorial(n) // n
        idx = k // num
        k = k % num

        if k == 0:
            answer.append(lst.pop(idx - 1))
        else:
            answer.append(lst.pop(idx))

        n -= 1

    return answer
