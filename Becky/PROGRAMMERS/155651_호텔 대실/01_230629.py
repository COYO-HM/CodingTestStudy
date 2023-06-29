# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/155651
def solution(book_time):
    book_time.sort()
    
    time = []
    for book in book_time:
        start, end = book
        a = int(start[:2]) * 60 + int(start[3:])
        b = int(end[:2]) * 60 + int(end[3:]) + 10
        time.append([a, b])
    
    room = [time[0]]
    answer = 1
    
    for i in range(1, len(time)):
        start_time, end_time = time[i][0], time[i][1]
        assigned = False
        
        for r in room:
            if start_time >= r[1]:
                r[0], r[1] = start_time, end_time
                assigned = True
                break
                
        if not assigned:
            room.append([start_time, end_time])
            answer += 1
    
    return answer