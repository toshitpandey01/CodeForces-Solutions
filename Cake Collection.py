def solve():
    t=int(input())
    for i in range(t):
        n,m=map(int,input().split())
        cakeoven=list(map(int,input().split()))
        cake=sum(ovenrate * m for ovenrate in cakeoven)
        print(cake)
solve()
