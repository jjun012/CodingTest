MOD = 10**9 + 9
n = int(input())

if n == 1:
    print(0)
else:
    result = 1
    for _ in range(n - 2):
        result = (result * 3) % MOD
    print((result * 2) % MOD)
