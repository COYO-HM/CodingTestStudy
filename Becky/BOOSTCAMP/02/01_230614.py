# 문제2
def solution(param0):
    dic = {"BOOL": 1, "SHORT": 2, "FLOAT": 4, "INT": 8, "LONG": 16} # 문자로 쓰면 헷갈려서 숫자로 변환
    answer = []
    numbers = []
    for param in param0:
        if param in dic:
            numbers.append(dic[param])

    ans = ''
    for num in numbers:
        # 8byte 넘어가는지 확인
        if len(ans) + num > 8:
            c = 8-len(ans)
            ans += "."*c
            answer.append(ans)
            ans = '' # 초기화

        if num == 1: # BOOL일 때
            ans += "#"

        elif num == 2: # SHORT일 때
            if len(ans) == 1:
                ans += ".##"
            else:
                ans += "##"

        elif num == 4: # FLOAT일 때
            if len(ans) == 1:
                ans += "...####"
            elif len(ans) == 2:
                ans += "..####"
            else:
                ans += "####"

        elif num == 8: # INT일 때
            ans += "########"
            answer.append(ans)
            ans = ''

        else: # LONG일 때
            ans += "########"
            answer.append(ans)
            answer.append(ans)
            ans = ''

    # 길이가 1이상인데 뒤에 숫자가 없는 경우 "."으로 패딩
    if len(ans) < 8 and len(ans) >= 1:
        c = 8-len(ans)
        ans += "."*c
        answer.append(ans)

    # 128byte 초과이면 HALT
    if len(answer) > 16:
        # print("HALT")
        return "HALT"
    else:
        print(answer)
        return answer

# solution(["INT", "INT", "BOOL", "SHORT", "LONG"])
# solution(["INT", "SHORT", "FLOAT", "INT","BOOL"])
# solution(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"])
# solution(["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"])