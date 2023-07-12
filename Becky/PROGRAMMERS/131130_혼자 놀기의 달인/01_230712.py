# https://school.programmers.co.kr/learn/courses/30/lessons/131130/
def solution(cards):
    visited = [False] * (len(cards) + 1)
    result = []

    for idx in cards:
        if not visited[idx]:
            temp = []
            if idx not in temp:
                temp.append(idx)
                idx = cards[idx - 1] # 해당 인덱스 상자로 이동
                visited[idx] = True
            result.append(len(temp))
        
    if result[0] == len(cards): # 상자가 다 열린 경우
        return 0

    result.sort(reverse=True)
    return result[0] * result[1]