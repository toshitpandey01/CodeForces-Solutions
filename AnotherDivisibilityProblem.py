import sys
input = sys.stdin.readline
def mybinpw(base, power, mod=10**9+7):
    ans = 1
    base %= mod
    while power > 0:
        if power % 2 == 1:
            ans = (ans * base) % mod
        base = (base * base) % mod
        power >>= 1
    return ans
t = int(input())
for _ in range(t):
    n = int(input())
    print(8 * n)
