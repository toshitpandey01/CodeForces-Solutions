n=int(input())
a=list(map(int,input().split()))
cost=0
neg=0
zero=0
for x in a:
    if x>1:
        cost+=x-1
    elif x<-1:
        cost+=abs(x+1)
        neg+=1
    elif x==0:
        zero+=1
    elif x==-1:
        neg+=1
if neg%2==1:
    if zero>0:
        cost+=zero
    else:
        cost+=zero+2
else:
    cost+=zero
print(cost)
