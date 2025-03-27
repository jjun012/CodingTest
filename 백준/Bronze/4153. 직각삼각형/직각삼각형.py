n=[]
n_max=0
while(True):
    n=list(map(int,input().split()))
    if (sum(n)==0):
        break

    n_max=max(n)
    n.remove(n_max)
    if (n_max**2)==(sum(x**2 for x in n)):
        print('right')
    else:
        print('wrong')

    
