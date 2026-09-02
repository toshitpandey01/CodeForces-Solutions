def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def next_prime(n):
    num=n+1
    while num<=50:
        if prime(num):
            return num
        num+= 1
n1,n2=map(int,input().split())
if n2==next_prime(n1):
    print("YES")
else:
    print("NO")

