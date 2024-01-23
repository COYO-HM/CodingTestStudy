# https://www.acmicpc.net/problem/20920
# 10:56-11:13
import sys

N, M = map(int, input().split())
words = dict()

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

words = sorted(words.items(), key=lambda x: ((-x[1], -len(x[0])), x[0]))

for word in words:
    print(word[0])
