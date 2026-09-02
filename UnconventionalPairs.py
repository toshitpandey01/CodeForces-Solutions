t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    max_diff=0
    for j in range(0,n,2):
        diff=a[j+1]-a[j]
        if diff>max_diff:
            max_diff=diff
    print(max_diff)
