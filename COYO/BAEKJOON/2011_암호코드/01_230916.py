import sys
input = sys.stdin.readline
n = input().rstrip()
ans = 0
c = 26
l = len(n)
dp = [0] * (l + 1)
dp[1] = 1 if "0" not in n else 0
dp[2] = sum([1 for j in range(l - 1) if 0 < int(n[j:j + 2]) <= 26])





print(dp)

print(ans % 1000000)