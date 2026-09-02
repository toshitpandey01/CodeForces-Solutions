a=input()
vovels={'a','e','i','o','u','y'}
ans=''
for i in a.lower():
    if i not in vovels:
        ans+="."+i
print(ans)
