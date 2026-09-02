def solve():
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        if a == b:
            print(0)
        else:
            print(1)
solve()
