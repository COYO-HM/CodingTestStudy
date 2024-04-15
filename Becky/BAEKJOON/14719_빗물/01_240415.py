# https://www.acmicpc.net/problem/14719
# 1h 24m
def calc(lst):
    global result
    l_idx, l_val = 0, lst[0]
    r_idx, r_val = len(lst) - 1, lst[-1]

    for i in range(1, r_idx + 1):
        if lst[i] >= l_val:
            r_idx, r_val = i, lst[i]
            s = (r_idx - l_idx - 1) * min(l_val, r_val)
            temp = 0
            for j in range(l_idx + 1, r_idx):
                temp += lst[j]
            result += s - temp

            l_idx, l_val = r_idx, r_val
            r_idx, r_val = len(lst) - 1, lst[-1]
    return result


h, w = map(int, input().split())
lst = list(map(int, input().split()))
max_idx, max_val = lst.index(max(lst)), max(lst)

result = 0
# 비가 고이는지 확인
check_rain = lst.count(0)
if check_rain == w or check_rain == w - 1:
    print(0)
else:
    l_lst, r_lst = lst[:max_idx + 1], lst[max_idx:][::-1]
    calc(l_lst)
    if len(r_lst) > 1:
        calc(r_lst)
    print(result)
