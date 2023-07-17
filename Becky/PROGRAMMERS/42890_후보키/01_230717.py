from itertools import combinations

def solution(relations):
    row, col = len(relations), len(relations[0])

    subsets = []
    for i in range(1, col+1):
        subsets.extend(combinations([j for j in range(col)], i)) # 원소 1개, 2개, 3개, ... i개 조합
        
    unique = []
    for subset in subsets:
        temp = [tuple([relation[i] for i in subset]) for relation in relations]
        if len(set(temp)) == row: # 유일성 검증
            is_True = True
            for u in unique: # 최소성 검증
                if set(u).issubset(set(subset)): # type이 tuple이여서 set으로 변경 후 확인
                    is_True = False
                    break
            if is_True:
                unique.append(subset)
    return len(unique)