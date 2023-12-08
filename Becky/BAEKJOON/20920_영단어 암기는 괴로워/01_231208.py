# https://www.acmicpc.net/problem/20920
# =====================================
# 로직 코드는 금방 짰는데 sys 사용이 익숙치 않아서 시간이 좀 더 걸림
# 시작: 22:10
# 종료: 22:42

import sys
N, M = map(int, input().split())
english_dict = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word in english_dict.keys():
            english_dict[word] += 1
        else:
            english_dict[word] = 1

english_lst = sorted(english_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in english_lst:
    print(word[0])
