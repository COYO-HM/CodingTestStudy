# https://www.acmicpc.net/problem/21921
# 초기화 신경 많이 쓸 것
# 시작: 20:50
# 종료: 21:15
N, X = map(int, input().split())
visitor = list(map(int, input().split()))

if max(visitor) == 0:
    print("SAD")
else:
    max_period = 1
    current_sum = sum(visitor[:X])
    max_visitor = current_sum
    for i in range(X, N):
        current_sum = current_sum - visitor[i - X] + visitor[i]
        if max_visitor < current_sum:
            max_visitor = current_sum
            max_period = 1
        elif max_visitor == current_sum:
            max_period += 1

    print(max_visitor)
    print(max_period)
