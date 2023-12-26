# https://www.acmicpc.net/problem/22233
# 17:43-17:53
import sys
N, M = map(int, input().split())
keywords = set(sys.stdin.readline().rstrip() for _ in range(N))

for _ in range(M):
    blog_post = set(sys.stdin.readline().rstrip().split(","))
    for word in blog_post:
        keywords.discard(word)
    print(len(keywords))