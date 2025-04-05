n=int(input())
x=list(map(int,input().split()))
result=0
sum=sum(x)
for i in range(0,n):
    sum=(sum-x[i])
    result+=(x[i]*sum)
    i+=1
print(result)