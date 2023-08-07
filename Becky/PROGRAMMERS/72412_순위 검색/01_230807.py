# https://school.programmers.co.kr/learn/courses/30/lessons/72412
# 정확성 통과 O 효율성 통과 X => for문 어떻게 개선할지 고민하기
def solution(info, query):
    # make string list 
    applicants = []
    for inform in info:
        applicants.append(inform.split(" "))
        
    condition = []
    for q in query:
        condition.append(q.replace(" and ", " ").split(" "))
    
    # search
    answer = []
    for i in range(len(condition)):
        cnt = 0
        for applicant in applicants:
            if int(applicant[4]) >= int(condition[i][4]):
                match = True
                for j in range(4):
                    if condition[i][j] != "-" and applicant[j] != condition[i][j]:
                        match = False
                        break
                if match:
                    cnt += 1
                    
        answer.append(cnt)
    
    return answer