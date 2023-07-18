# https://school.programmers.co.kr/learn/courses/30/lessons/172927
def solution(picks, minerals):
    # 5개씩 광물 묶기
    # 곡괭이를 모두 사용해도 광물이 남은 경우를 처리하기 위해 min 함수 사용
    minerals = [list(minerals[i:i+5]) for i in range(0, min(sum(picks) * 5, len(minerals)), 5)]
    scores = []
    
    # 곡괭이 종류에 따른 광물 피로도 계산
    for m in minerals:
        tmp = [0, 0, 0]
        for i in m:
            tmp[0] += 1
            tmp[1] += 5 if i == "diamond" else 1
            tmp[2] += 25 if i == "diamond" else 5 if i == "iron" else 1
        scores.append(tmp)
    # 내림차순 정렬
    scores.sort(key=lambda x:(-x[2],-x[1]))
    
    answer = 0
    for score in scores:
        if picks[0]:
            answer += score[0]
            picks[0] -= 1
        elif picks[1]:
            answer += score[1]
            picks[1] -= 1
        elif picks[2]:
            answer += score[2]
            picks[2] -= 1
        else:
            break
            
    return answer