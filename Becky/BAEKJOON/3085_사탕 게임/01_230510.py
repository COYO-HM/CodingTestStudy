# 문제: https://www.acmicpc.net/problem/3085
def check(data):
    m_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if data[i][j] == data[i][j-1]: # 열 체크
                cnt += 1
            else:
                cnt = 1
            m_cnt = max(m_cnt, cnt)

        cnt = 1
        for j in range(1, n):
            if data[j][i] == data[j-1][i]: # 행 체크
                cnt += 1
            else:
                cnt = 1
            m_cnt = max(m_cnt, cnt)
    return m_cnt

n = int(input())
data = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n: # 열 체크
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
            cnt = check(data)
            ans = max(ans, cnt)
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]

        if i + 1 < n: # 행 체크
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
            cnt = check(data)
            ans = max(ans, cnt)
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]

print(ans)