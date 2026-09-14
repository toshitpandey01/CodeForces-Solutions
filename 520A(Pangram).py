n=int(input())
word=input().lower()
count=0
if len(set(word))==26:
    print("YES")
else:
    print("NO")