# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    kakao_type = ["R", "T", "C", "F", "J", "M", "A", "N"]
    kakao_dic = dict()
    for k_t in kakao_type:
        kakao_dic[k_t] = 0

    for i in range(len(survey)):
        disagree, agree = survey[i][0], survey[i][1]
        choice = choices[i]

        if choice > 4:
            kakao_dic[agree] += choice - 4
        elif choice < 4:
            kakao_dic[disagree] += 4 - choice

    answer = ''
    if kakao_dic["R"] >= kakao_dic["T"]:
        answer += "R"
    else:
        answer += "T"

    if kakao_dic["C"] >= kakao_dic["F"]:
        answer += "C"
    else:
        answer += "F"

    if kakao_dic["J"] >= kakao_dic["M"]:
        answer += "J"
    else:
        answer += "M"

    if kakao_dic["A"] >= kakao_dic["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer