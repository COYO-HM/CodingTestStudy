def solution(arr):
    ans = ""
    for b in arr:
        l = len(ans)
        if b == "BOOL":
            ans += "#"
        elif b == "SHORT":
            ans += "." * (l % 2) + "##"
        elif b == "FLOAT":
            if l % 4 != 0:
                ans += "." * (4 - (l % 4))
            ans += "####"
        elif b == "INT":
            if l % 8 != 0:
                ans += "." * (8 - (l % 8))
            ans += "########"
        elif b == "LONG":
            if l % 8 != 0:
                ans += "." * (8 - (l % 8))
            ans += "#" * 16

    if len(ans) > 128:
        print("HALT")
        return
    if len(ans) % 8 != 0:
        ans += "." * (8 - len(ans) % 8)

    print(", ".join([ans[i: i + 8] for i in range(0, len(ans), 8)]))

solution(["INT", "INT", "BOOL", "SHORT", "LONG"])
solution(["INT", "SHORT", "FLOAT", "INT", "BOOL"])
solution(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"])
solution(["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"])