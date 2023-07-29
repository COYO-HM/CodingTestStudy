from collections import deque

def time_to_minutes(start_time):
    h, m = map(int, start_time.split(":"))
    return h * 60 + m

def solution(plans):
    answer = []
    plans = [(name, time_to_minutes(start_time), int(spend_time)) for name, start_time, spend_time in plans]
    plans = sorted(plans, key=lambda x: x[1])  # 시작 시간 기준으로 정렬
    
    que = deque()
    left_time = 0
    
    for i in range(len(plans)):
        name, start_time, spend_time = plans[i]
        
        while que:
            q_name, remain_time = que.pop()
            
            if left_time >= remain_time:
                left_time -= remain_time
                answer.append(q_name)
            else:
                que.append((q_name, remain_time - left_time))
                break
        que.append((name, spend_time))
        
        if i < len(plans) - 1:
            next_start = plans[i + 1][1]
            left_time = next_start - start_time
        
    while que:
        q_name, remain_time = que.pop()
        answer.append(q_name)
    
    return answer
    