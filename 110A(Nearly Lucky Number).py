n=input()
count=sum(c=='4' or c=='7' for c in n)
if count==4 or count==7:
    print("YES")
else:
    print("NO")