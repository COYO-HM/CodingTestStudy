# https://www.acmicpc.net/problem/14719
# 00:13:32

import sys

input = sys.stdin.readline
total_h, total_w = map(int, input().split())
blocks = list(map(int, input().split()))
sorted_blocks = sorted([(h, idx) for idx, h in enumerate(blocks)], reverse=True)
answer = [0] * total_w

prev_idx = 0
for idx in range(1, total_w):
    h = min(sorted_blocks[prev_idx][0], sorted_blocks[idx][0])
    left_x = min(sorted_blocks[prev_idx][1], sorted_blocks[idx][1])
    right_x = max(sorted_blocks[prev_idx][1], sorted_blocks[idx][1])
    for x in range(left_x, right_x + 1):
        answer[x] = max(h - blocks[x], answer[x])
    prev = idx


# print(answer)
print(sum(answer))