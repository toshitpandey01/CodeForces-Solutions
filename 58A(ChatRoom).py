a=input().strip()
word="hello"
count=0
for character in a:
    if character==word[count]:
        count=count+1
        if count==len(word):
            break
if count == len(word):
    print("YES")
else:
    print("NO")
