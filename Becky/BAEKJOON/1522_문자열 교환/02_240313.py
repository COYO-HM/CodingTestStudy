# https://www.acmicpc.net/problem/1522
# 20:53-21:34

s = input()
a = s.count('a')

s += s[0: a - 1]
cnt = float('inf')

for i in range(len(s) - a + 1):
    cnt = min(cnt, s[i: i + a].count('b'))
print(cnt)
