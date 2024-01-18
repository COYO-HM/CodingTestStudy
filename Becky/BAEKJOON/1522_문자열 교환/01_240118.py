# https://www.acmicpc.net/problem/1522
# 11:33-12:09
import sys

s = sys.stdin.readline().rstrip()
cnt_a = s.count('a')

s += s[0: cnt_a - 1]
min_val = float('inf')
for i in range(len(s) - cnt_a + 1):
    min_val = min(min_val, s[i: i + cnt_a].count('b'))
print(min_val)
