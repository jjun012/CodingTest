n,m=map(int,input().split())
coins=[]
cnt=0
for i in range(n):
    a=int(input())
    coins.append(a)

coins.sort(reverse=True)
for coin in coins:
    cnt +=m//coin
    m%=coin

print(cnt)