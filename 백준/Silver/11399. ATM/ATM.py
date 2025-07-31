n=int(input())

peo=list(map(int,input().split()))

peo.sort()
ans=0

for i in range(1,n+1):
    ans+=sum(peo[0:i])
print(ans)