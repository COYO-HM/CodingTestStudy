# 문제: https://www.acmicpc.net/problem/1935
n = int(input()) # 피연산자 개수
postfix = input() # 후위 표기식
operand = [int(input()) for _ in range(n)] # 피연산자 대응값 리스트

operator = ["*", "/", "+", "-"]
stack = []
for p in postfix:
    if p not in operator:
        stack.append(operand[ord(p)-ord('A')]) # ord(str) => unicode num

    else:
        b = stack.pop()
        a = stack.pop()

        stack.append(eval(str(a) + p + str(b))) # eval(연산식) string타입 연산 가능

print("%.2f" %stack[0])
