# https://www.acmicpc.net/problem/20310
# 출력 형식 제대로 안 봐서 틀림
# 23:28 - 00:07

import sys
S = list(sys.stdin.readline().rstrip())
zero_cnt, one_cnt = S.count('0') // 2, S.count('1') // 2

check_point = 0
for i in S:
    if check_point == one_cnt:
        break

    if i == '1':
        S.remove(i)
        check_point += 1

check_point = 0
for i in range(len(S) - 1, 0, -1):
    if check_point == zero_cnt:
        break

    if S[i] == '0':
        S.pop(i)
        check_point += 1

print(''.join(S))