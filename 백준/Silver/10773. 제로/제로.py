n=int(input())

arr=[]
for i in range(n):
    
    a=int(input())
    if a==0:
        del arr[-1]
    else:
        arr.append(a)
    
print(sum(arr))