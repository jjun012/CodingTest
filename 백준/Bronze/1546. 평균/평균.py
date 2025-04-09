n=int(input())
grade=list(map(int,input().split()))
m=max(grade)
for i in range(n):
    grade[i]=(grade[i]/m)*100
sum=0
for i in range(n):
    sum+=grade[i]

print(sum/n)
