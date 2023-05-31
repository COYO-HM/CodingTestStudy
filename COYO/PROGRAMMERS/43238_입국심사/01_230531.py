def solution(n, times):
    answer = 0
    s, e = 0, max(times) * n
    while s <= e:
        m = (s + e) // 2
        p = 0
        for t in times:
            p += m // t
            if p >= n:
                break

        if p >= n:
            e = m - 1
            answer = m
        else:
            s = m + 1


    return answer