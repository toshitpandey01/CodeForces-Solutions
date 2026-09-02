t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    x_list=list(map(int, input().split()))
    left=x_list[0]
    right=x_list[-1]
    min_steps=min(abs(s-left),abs(s-right))+(right-left)
    print(min_steps)
