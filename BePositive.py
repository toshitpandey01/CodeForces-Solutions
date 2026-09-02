t=int(input().strip())
for i in range(t):
    n=int(input().strip())
    values=list(map(int, input().strip().split()))
    negative_ones=0
    zeros=0
    for val in values:
        if val==-1:
            negative_ones+=1
        elif val==0:
            zeros+=1
    answer=zeros+2*(negative_ones%2)
    print(answer)
