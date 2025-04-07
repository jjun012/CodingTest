n=int(input())
num=list(map(int,input().split()))
t,p=map(int,input().split())
t_cnt=0

for i in range(len(num)):
    if num[i]==0:
        continue
    elif t>=num[i]:
        t_cnt+=1
    
    else:
        if num[i]%t==0:
            t_cnt+=num[i]//t
        else:
            t_cnt+=num[i]//t
            t_cnt+=1
print(t_cnt)
print(n//p,n%p)

