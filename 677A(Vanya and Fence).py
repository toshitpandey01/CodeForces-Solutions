n,h=map(int,input().split())
a=map(int,input().split())
width=0
for height in a:
    if height>h:
        width=width+2
    else:
        width=width+1
print(width)
