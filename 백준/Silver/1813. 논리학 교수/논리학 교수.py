n=int(input())
list=list(map(int,input().split()))
list.sort(reverse=True)
cnt=0
if n==1:
    if list[0]==0:
        print(-1)
    
    elif list[0]==1:
        print(1)
    else:
        print(0)
else:
    for i in list:
        cnt+=1
        if i==0:
            print(-1)
            break
        if i==list.count(i):
            print(i)
            break 
        if cnt == len(list):
            print(0)
            break
