# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/135807
import math
def check(array, gcd): # 조건 확인
    for num in array:
        if num % gcd == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0
    
    gcd_A, gcd_B = arrayA[0], arrayB[0]
    
    for a in arrayA: gcd_A = math.gcd(a, gcd_A) # arrayA 최대공약수 구하기
    for b in arrayB: gcd_B = math.gcd(b, gcd_B) # arrayB 최대공약수 구하기
        
    if check(arrayA, gcd_B): answer = max(answer, gcd_B) # 조건1 확인
    if check(arrayB, gcd_A): answer = max(answer, gcd_A) # 조건2 확인
    
    return answer