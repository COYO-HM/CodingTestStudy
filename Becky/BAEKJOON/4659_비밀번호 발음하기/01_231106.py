# https://www.acmicpc.net/problem/4659
consonants = "aeiou"
vowels = "bcdfghjklmnpqrstvwxyz"


def check_acceptable(password):
    # 자음 1개 이상 포함 여부 확인
    consonants_cnt = sum(1 for char in password if char in consonants)

    # 자음 or 모음이 3개 연속인지 확인
    for i in range(len(password) - 2):
        s = password[i: i + 3]
        if all(char in consonants for char in s):
            return False
        if all(char in vowels for char in s):
            return False

    for j in range(len(password) - 1):
        if password[j] == password[j + 1] and password[j] not in "eo":
            return False

    return consonants_cnt > 0


while True:
    tc = input()
    if tc == "end":
        break

    result = check_acceptable(tc)

    if result is False:
        print(f"<{tc}> is not acceptable.")
    else:
        print(f"<{tc}> is acceptable.")
