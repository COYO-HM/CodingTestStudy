# https://www.acmicpc.net/problem/2607
# 11:31-
N = int(input())
ans = 0
first_word = list(input())

for _ in range(N - 1):
    word = input()
    temp = first_word[:]
    cnt = 0

    for w in word:
        if w in temp:
            temp.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(temp) < 2:
        ans += 1

print(ans)
