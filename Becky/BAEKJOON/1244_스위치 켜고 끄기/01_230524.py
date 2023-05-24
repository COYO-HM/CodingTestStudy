n = int(input())
status = [-1] + list(map(int, input().split()))
students = int(input())

def change(n):
    if status[n] == 0:
        status[n] = 1
    else:
        status[n] = 0
    return

for _ in range(students):
    gender, num = map(int, input().split())

    # 남학생인 경우
    if gender == 1:
        for i in range(num, n+1, num):
            change(i)

    # 여학생인 경우
    else:
        change(num)

        for j in range(n//2):
            if (num+j > n) or (num-j < 1): break
            if status[num+j] == status[num-j]:
                change(num+j)
                change(num-j)
            else: break

for i in range(1, n+1):
    print(status[i], end = " ")
    if i % 20 == 0:
        print()
