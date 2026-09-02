t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    c=[0]*n
    possible=True
    for k in range(n,0,-1):
        found=False
        for start in range(n-k+1):
            if all(c[i]+1<=p[i] for i in range(start,start+k)):
                for i in range(start,start+k):
                    c[i]+=1
                found=True
                break
        if not found:
            possible=False
            break
    print("YES" if possible else "NO")
