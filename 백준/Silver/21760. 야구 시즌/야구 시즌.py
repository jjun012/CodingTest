for i in range(int(input())):
    n, m, a, b = map(int, input().split())
    x = 2*b//(a*n*m*(m-1) + m*m*n*(n-1))
    if x:
        print(m*(m-1)*n*a*x//2 + m*m*n*(n-1)*x//2)
    else:
        print(-1)