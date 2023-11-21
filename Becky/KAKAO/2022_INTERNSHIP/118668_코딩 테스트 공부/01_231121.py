# https://school.programmers.co.kr/learn/courses/30/lessons/118668

def solution(alp, cop, problems):
    answer = 0
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    dp = [[float("inf")] * (max_cop + 1) for _ in range(max_alp + 1)]

    dp[alp][cop] = 0

    for r in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            if r < max_alp:
                dp[r + 1][c] = min(dp[r + 1][c], dp[r][c] + 1)
            if c < max_cop:
                dp[r][c + 1] = min(dp[r][c + 1], dp[r][c] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if r >= alp_req and c >= cop_req:
                    new_alp = min(r + alp_rwd, max_alp)
                    new_cop = min(c + cop_rwd, max_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[r][c] + cost)

    return dp[max_alp][max_cop]