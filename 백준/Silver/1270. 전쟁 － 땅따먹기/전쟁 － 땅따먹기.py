from collections import Counter
n=int(input())

for i in range(n):
    a=list(map(int,input().split()))
    n=a[0]
    a.pop(0)
    m=(Counter(a).most_common(1))
    if m[0][1]<=n/2:
        print("SYJKGW")
    else:
        print(m[0][0])
    
