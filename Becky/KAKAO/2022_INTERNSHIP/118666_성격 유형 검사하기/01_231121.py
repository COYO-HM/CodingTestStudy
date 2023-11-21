# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    kakao_type = ["R", "T", "C", "F", "J", "M", "A", "N"]
    kakao_dic = {k_t: 0 for k_t in kakao_type}

    for i, (disagree, agree) in enumerate(survey):
        choice = choices[i]

        if choice > 4:
            kakao_dic[agree] += choice - 4
        elif choice < 4:
            kakao_dic[disagree] += 4 - choice

    answer = ""
    for first, second in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        if kakao_dic[first] >= kakao_dic[second]:
            answer += first
        else:
            answer += second

    return answer