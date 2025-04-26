n,m=map(int,input().split())
list=list(map(int,input().split()))
total=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum=list[i]+list[j]+list[k]
            if sum<=m:
                total.append(sum)

print(max(total))
