n=int(input())
i=map(int,input().split())
count=sum(c==1 for c in i)
if count>=1:
    print("HARD")
else:
    print("Easy")
