n=int(input())
result=1
cnt=0

for i in range(1,n+1,1):
    result *=i
result=str(result)
for i in range(len(result)):
    if result[-1 -i]!='0':
        break
    cnt+=1

print(cnt)