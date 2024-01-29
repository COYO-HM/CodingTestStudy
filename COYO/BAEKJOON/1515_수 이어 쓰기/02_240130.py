# https://www.acmicpc.net/problem/1515
# 00:34:32

import sys

input = sys.stdin.readline
nums = input().rstrip()
N, nums_idx, nums_len = 0, 0, len(nums)

while nums:
    N = N + 1
    n_str = str(N)
    n_len = len(n_str)
    idx = 0
    while idx < n_len and len(nums):
        n = nums[0]
        if n == n_str[idx]:
            nums = nums[1:]
        idx += 1

print(N)
