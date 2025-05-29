n=int(input())
arr=set()
cnt=0
for i in range(n):
    a,b=map(int,input().split())
    if b==1:
        if a in arr:
            cnt+=1
        arr.add(a)
    else:
        if a not in arr:
            cnt+=1
        else:
            arr.remove(a)

print(len(arr)+cnt)