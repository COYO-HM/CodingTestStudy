# 문제: https://www.acmicpc.net/problem/1316
n = int(input())
cnt = 0

for tc in range(n):
    stack = []
    words = list(input())

    for alp in words:
        if stack:
            p = stack.pop()
            if (p == alp) or (alp not in stack):
                stack.append(p)
                stack.append(alp)
            else:
                stack = []
                break
        else:
            stack.append(alp)

    if stack:
        cnt += 1
    else:
        pass
print(cnt)
