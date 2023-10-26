# https://www.acmicpc.net/problem/1157
s = input()
s = s.upper()
dictionary = {}

for val in s:
    if val not in dictionary:
        dictionary[val] = 1
    else:
        dictionary[val] += 1

m = max(dictionary.values())

answer = []
for idx, val in dictionary.items():
    if val == m:
        answer.append(idx)

print("?") if len(answer) > 1 else print(answer[0])
