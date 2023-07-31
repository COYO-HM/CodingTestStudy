# https://school.programmers.co.kr/learn/courses/30/lessons/12923
# tc 13, 효율성 테스트 통과 X
def solution(begin, end):
    def check(x):
        if x == 1:
            return 0
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                if x //i > max_val:
                    continue
                else:
                    return x // i
        return 1
    
    max_val = 10000001
    answer = []
    for i in range(begin, end + 1):
        answer.append(check(i))
    return answer
