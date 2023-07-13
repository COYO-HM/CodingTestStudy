def solution(data, col, row_begin, row_end):
    
    # data[col-1]로 오름차순, data[0]으로 내림차순 정렬
    data.sort(key=lambda x: [x[col - 1], -x[0]])
    
    answer = 0
    for i in range(row_begin, row_end + 1):
        S_sum = 0
        for j in data[i - 1]:
            S_sum += (j % i)
        answer ^= S_sum # bitwise XOR 연산
    
    return answer