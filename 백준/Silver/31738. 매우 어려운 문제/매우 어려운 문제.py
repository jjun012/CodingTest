import sys
n,m=map(int,sys.stdin.readline().split())

if n >=m:
    print(0)
else:
    num=1
    for i in range(1,n+1):
        num*=i
        num%=m
    print(num)