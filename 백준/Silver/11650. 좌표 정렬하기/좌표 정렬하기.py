n=int(input())
arr=[]
for i in range(n):
    n,m=map(int,input().split())
    arr.append([n,m])
arr.sort(key=lambda x:[x[0],x[1]])

for i,j in arr:
    print(i,j)