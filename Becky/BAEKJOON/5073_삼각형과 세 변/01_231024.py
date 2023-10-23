# https://www.acmicpc.net/problem/5073
while True:
    triangle = list(map(int, input().split()))
    triangle.sort()
    a, b, c = triangle[0], triangle[1], triangle[2]
    if (a, b, c) == (0, 0, 0):
        break

    if a + b <= c:
        print("Invalid")
    elif (a == b) and (b == c):
        print("Equilateral")
    elif (a == b) or (b == c) or (c == a):
        print("Isosceles")
    else:
        print("Scalene")