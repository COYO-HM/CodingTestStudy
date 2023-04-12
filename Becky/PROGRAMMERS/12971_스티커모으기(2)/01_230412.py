def solution(sticker):
    l = len(sticker)
    if l == 1:
        return sticker[0]

    # 스티커를 떼는 경우
    arr = [0 for _ in range(l)]
    arr[0] = sticker[0]
    arr[1] = sticker[0]
    for i in range(2, l - 1):
        arr[i] = max(arr[i - 1], arr[i - 2] + sticker[i])
    val = max(arr)

    # 스티커를 떼지 않는 경우
    arr = [0 for _ in range(l)]
    arr[1] = sticker[1]
    for i in range(2, l):
        arr[i] = max(arr[i - 1], arr[i - 2] + sticker[i])

    return max(val, max(arr))
