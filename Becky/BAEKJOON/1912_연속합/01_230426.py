n = int(input())
lst = list(map(int, input().split()))

res = [lst[0]]
for i in range(len(lst)-1):
    res.append(max(res[i]+lst[i+1], lst[i+1]))
print(max(res))
