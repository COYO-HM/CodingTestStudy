# https://www.acmicpc.net/problem/7490
# +, -, ''
# +는 더하기, -는 빼기 ''는 숫자 이어붙이기 => 0이 되면 출력
# ASCII 순서에 따라 모든 수식을 출력하려면 문자열 리스트로 저장?

def dfs(n, idx, r):
    if idx == N:
        ans = eval(r.replace(' ', ''))
        if ans == 0:
            ans_lst.append(r)
        return
    else:
        next_idx = idx + 1
        dfs(n, next_idx, r + ' ' + str(next_idx))
        dfs(n, next_idx, r + '+' + str(next_idx))
        dfs(n, next_idx, r + '-' + str(next_idx))


for _ in range(int(input())):
    N = int(input())
    lst = [i for i in range(1, N + 1)]
    ans_lst = []
    dfs(N, 1, '1')
    for a in ans_lst:
        print(a)
    print()
