def solution(sticker):
    size = len(sticker)
    if size == 1:
        return sticker[0]


    dp0 = [0] * size
    dp1 = [0] * size
    dp0[0] = sticker[0]
    dp0[1] = sticker[0]
    dp1[1] = sticker[1]


    for i in range(2, len(sticker) - 1):
        dp0[i] = max(dp0[i - 2] + sticker[i], dp0[i - 1])
    for i in range(2, len(sticker)):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])

    print(dp0)
    print(dp1)


    answer = 0
    return answer