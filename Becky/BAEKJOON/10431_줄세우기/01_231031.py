# https://www.acmicpc.net/problem/10431
P = int(input()) # 테스트 케이스 수
for _ in range(P):
    students = list(map(int, input().split()))
    tc_number = students.pop(0)  # 첫 번째로 입력 받은 숫자가 tc 번호

    stack = []
    count_move = 0
    for i in range(1, 20):
        for j in range(i - 1, -1, -1):
            if students[j] > students[i]:
                count_move += 1

    print(tc_number, count_move)
