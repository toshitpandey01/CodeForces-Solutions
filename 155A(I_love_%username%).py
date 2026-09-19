n=int(input())
score=list(map(int,input().split()))
max=score[0]
min=score[0]
count=0
for score in score[1:]:
    if score>max:
        max=score
        count=count+1
    elif score<min:
        min=score
        count=count+1
print(count)