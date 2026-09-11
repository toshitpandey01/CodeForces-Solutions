n=int(input())
fx=0
for i in range(1,n+1):
    if i%2==0:
        fx=fx+i
    else:
        fx=fx-i
print(fx)
