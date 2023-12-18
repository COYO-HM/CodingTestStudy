# https://www.acmicpc.net/problem/2607
# 21:08-22:29
import sys

words = [sys.stdin.readline().rstrip() for _ in range(int(input()))]
first_word = list(words[0])

result = 0
for word in words[1:]:
    temp = first_word[:]
    cnt = 0

    for w in word:
        if w in temp:
            temp.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(temp) < 2:
        result += 1

print(result)
