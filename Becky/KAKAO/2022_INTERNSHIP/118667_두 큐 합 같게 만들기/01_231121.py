# https://school.programmers.co.kr/learn/courses/30/lessons/118667#
from collections import deque


def solution(queue1, queue2):
    que1, que2 = deque(queue1), deque(queue2)
    total_sum = sum(que1) + sum(que2)

    if total_sum % 2 != 0:
        return -1

    count = 0
    sum_que1, sum_que2 = sum(que1), sum(que2)
    while que1:
        if count > 600000:
            return -1

        diff = sum_que1 - sum_que2
        if diff == 0:
            return count

        if diff < 0:
            val = que2.popleft()
            sum_que2 -= val
            que1.append(val)
            sum_que1 += val
        else:
            val = que1.popleft()
            sum_que1 -= val
            que2.append(val)
            sum_que2 += val
        count += 1

    return -1
