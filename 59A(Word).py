s=input()
c1=sum(c.isupper() for c in s)
c2=sum(c.islower() for c in s)
if c1>c2:
    print(s.upper())
else:
    print(s.lower())