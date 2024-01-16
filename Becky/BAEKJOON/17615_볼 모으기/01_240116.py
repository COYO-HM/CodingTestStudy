# https://www.acmicpc.net/workbook/view/8708
# 17:12-18:00
import sys
input = sys.stdin.readline
N = int(input())
balls = str(input().rstrip())
cnt = []

# 같은 색인 볼은 한번에 지운 후 남은 볼 세기
right_red = balls.rstrip('R')
cnt.append(right_red.count('R'))

right_blue = balls.rstrip('B')
cnt.append(right_blue.count('B'))

left_red = balls.lstrip('R')
cnt.append(left_red.count('R'))

left_blue = balls.lstrip('B')
cnt.append(left_blue.count('B'))

print(min(cnt))