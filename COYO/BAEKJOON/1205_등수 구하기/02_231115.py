import sys
input = sys.stdin.readline
N, new_score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    answer = -1
    rank = 1
    for idx, s in enumerate(scores):
        if idx >= P or s <= new_score:
            break
        elif s > new_score:
            rank += 1

    if N < P or scores[-1] < new_score:
        answer = rank
    print(answer)