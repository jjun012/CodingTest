n,m=map(int,input().split())
add={}

for i in range(n):
    s,ps=input().split()
    add[s]=ps
for i in range(m):
    print(add[input().rstrip()])