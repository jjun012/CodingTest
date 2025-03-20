m= int(input())
list=list(map(int,input().split()))

jm=m
jj=0
for i in list:
    if jm >=i:
        jj+=jm//i
        jm=jm%i

sm=m
sj=0
for i in range(3,len(list)):
    if(list[i-3]>list[i-2])and(list[i-2]>list[i-1])and(list[i-1]>list[i]):
        if sm>=list[i]:
            sj += sm//list[i]
            sm = sm%list[i]

jsum=jm+(jj*list[-1])
ssum=sm+(sj*list[-1])
if jsum >ssum:
    print("BNP")
elif jsum<ssum:
    print("TIMING")
else:
    print("SAMESAME")

