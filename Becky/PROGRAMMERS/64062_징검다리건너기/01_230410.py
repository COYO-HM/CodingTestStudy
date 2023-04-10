# 정확성 테스트만 맞았음
def solution(stones, k):
    ans = 0
    while True:
        ans += 1
        for i in range(len(stones)):
            if stones[i] == 0:
                continue
            else:
                stones[i] -= 1

        cnt = 0
        for stone in stones:
            if stone == 0:
                cnt += 1
                if cnt == k:
                    return ans
            else:
                cnt = 0
    return ans
