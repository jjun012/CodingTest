n,m=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
a.sort(key=lambda x:(x%10!=0,x))
for i in range(n):
    if a[i]==10:
        cnt+=1
    elif a[i]>10:
        while a[i]>10 and m>0:
            a[i]-=10
            cnt+=1
            m-=1
            if a[i]==10:
                cnt+=1
            
            
print(cnt)
        
            
        

        




    
