n, m = map(int, input().split())
li=[]
wa=[]
for i in range(n):
    a=input()
    li.append(a)
for i in range(m):
    a=input()
    wa.append(a)
set1=set(li)
set2=set(wa)
dup=list(set1.intersection(set2))
print(len(dup))
dup.sort()
for i in range(len(dup)):
    print(dup[i])