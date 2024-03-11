# https://www.acmicpc.net/problem/17615
# 12:46-13:03
N = int(input())
balls = str(input())  # 공
cnt = []

r_red = balls.rstrip('R')
cnt.append(r_red.count('R'))

r_blue = balls.rstrip('B')
cnt.append(r_blue.count('B'))

l_red = balls.lstrip('R')
cnt.append(l_red.count('R'))

l_blue = balls.lstrip('B')
cnt.append(l_blue.count('B'))

print(min(cnt))
