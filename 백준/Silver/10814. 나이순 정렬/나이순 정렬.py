n=int(input())
arr=[]
for i in range(n):
    n,m=input().split()
    arr.append([int(n),m])

arr.sort(key=lambda x:x[0])
for i,j in arr:
    print(i,j)