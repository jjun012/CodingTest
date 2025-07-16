import sys
A,B,D=map(int,sys.stdin.readline().split())
list=[False,False]+[True]*4000000
cnt=0
for i in range(2,4000000):
    if list[i]:
        for j in range(i+i,4000000,i):
            list[j]=False

for i in range(A,B+1):
    if list[i]:
        if str(D) in str(i):
            cnt+=1
print(cnt)
