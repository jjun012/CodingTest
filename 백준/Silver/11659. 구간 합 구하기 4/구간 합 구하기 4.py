import sys
input=sys.stdin.readline

n,m=map(int,input().split())
num=list(map(int,input().split()))
sum=[0]
result=0

for i in num:
    result+=i
    sum.append(result)

for i in range(m):
    a,b=map(int,input().split())
    print(sum[b]-sum[a-1])
