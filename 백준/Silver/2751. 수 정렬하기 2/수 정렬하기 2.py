n=int(input())
num=[]
for i in range(n):
    a=int(input())
    num.append(a)
num.sort()
for i in range(n):
    print(num[i])