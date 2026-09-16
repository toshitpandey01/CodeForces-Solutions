n=int(input())
event=map(int,input().split())
officers=0
untreated=0
for i in event:
    if i==-1:
        if officers>0:
            officers=officers-1
        else:
            untreated=untreated+1
    else:
        officers=officers+i
print(untreated)