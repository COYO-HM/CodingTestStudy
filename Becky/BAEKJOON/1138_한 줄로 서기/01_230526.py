# 문제:  https://www.acmicpc.net/problem/1138
n = int(input())
bigger = list(map(int, input().split())) # 자신보다 키 큰 사람 수
answer = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == bigger[i] and answer[j] == 0: # 빈 자리 = 자신보다 키 큰 사람 수일 때
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            cnt += 1 # 빈 자리 세기

print(*answer)
