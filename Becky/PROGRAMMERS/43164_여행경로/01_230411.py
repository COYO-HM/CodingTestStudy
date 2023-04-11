def solution(tickets):
    airline = {}
    for s, e in tickets:
        airline[s] = e

    airline = dict(sorted(airline.items()))

    ans = []
    path = ["ICN"]

    while path:
        now = path[-1]

        if now not in airline or len(airline[now]) == 0:
            ans.append(path.pop())
        else:
            path.append(airline[now].pop())

    return ans[::-1]
