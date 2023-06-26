# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations

def calculate(num1, num2, operator):
    if operator == "+": return num1 + num2
    elif operator == "-": return num1 - num2
    elif operator == "*": return num1 * num2

def solution(expression):
    operators = ["+", "-", "*"]
    expression = expression.replace("+", " + ")
    expression = expression.replace("-", " - ")
    expression = expression.replace("*", " * ")
    expression = expression.split()
    
    answer = 0
    
    # 연산자가 2개인 경우 처리
    if len(set(expression) & set(operators)) == 2:
        priorities = [[op1, op2] for op1, op2 in permutations(operators, 2)]
    else:
        priorities = list(permutations(operators, 3))
        
    for priority in priorities:
        temp_expression = expression[:] # expression 복사
        
        for operator in priority:
            while operator in temp_expression:
                idx = temp_expression.index(operator)
                num1 = int(temp_expression[idx - 1])
                num2 = int(temp_expression[idx + 1])
                
                result = calculate(num1, num2, operator)
                temp_expression = temp_expression[:idx - 1] + [str(result)] + temp_expression[idx + 2:]
                
        answer = max(answer, abs(int(temp_expression[0])))
    

    return answer