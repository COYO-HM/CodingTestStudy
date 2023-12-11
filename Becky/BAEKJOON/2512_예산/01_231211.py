# https://www.acmicpc.net/problem/2512
# 시작: 20:08
# 종료: 20:33
import sys
N = int(input())
request_money = list(map(int, sys.stdin.readline().split()))
budget = int(input())

sum_of_request = sum(request_money)
if budget >= sum_of_request:
    print(max(request_money))
else:
    l = 0
    r = max(request_money)
    result = 0

    while l <= r:
        mid = (l + r) // 2

        money_sum = 0
        for money in request_money:
            money_sum += min(money, mid)

        if money_sum <= budget:
            result = mid
            l = mid + 1
        else:
            r = mid - 1

    print(result)
