a,b,v=map(int,input().split())
cnt=0
day=0
if (v-b)%(a-b)==0:
    print(int((v-b)/(a-b)))
else:
    print(int((v-b)/(a-b))+1)

    