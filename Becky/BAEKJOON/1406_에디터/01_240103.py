# https://www.acmicpc.net/problem/1406
# 14:00-14:36(1차 시간 초과)
# 자료 구조 생각할 것
import sys
import collections
s = list(sys.stdin.readline().rstrip())
que = collections.deque()

for _ in range(int(input())):
    order = list(sys.stdin.readline().split())

    if order[0] == 'L':
        if s:
            que.appendleft(s.pop())

    elif order[0] == 'D':
        if que:
            s.append(que.popleft())

    elif order[0] == 'B':
        if s:
            s.pop()

    else:
        s.append(order[1])

s.extend(que)
print(''.join(s))

