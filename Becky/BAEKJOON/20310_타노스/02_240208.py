# https://www.acmicpc.net/problem/20310
# 21:37-21:53
S = list(map(str, input()))
zero, one = S.count("0") // 2, S.count("1") // 2
for _ in range(one):
    S.remove("1")

S = S[::-1]
for _ in range(zero):
    S.remove("0")

ans = S[::-1]
print("".join(ans))
