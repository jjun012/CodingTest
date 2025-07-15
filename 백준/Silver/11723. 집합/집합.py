import sys
n= int(sys.stdin.readline())
hap=[]
for i in range(n):
    a=sys.stdin.readline().split()

    if a[0]=='add':
        if a[1] in hap:
            continue
        else:
            hap.append(a[1])
    if a[0]=='remove':
        if a[1] in hap:
            hap.remove(a[1])
        else:
            continue
    if a[0]=='check':
        if a[1] in hap:
            print(1)
        else:
            print(0)
    if a[0]=='toggle':
        if a[1] in hap:
            hap.remove(a[1])
        else:
            hap.append(a[1])
    if a[0]=='all':
        hap.clear()
        for j in range(1,21):
            hap.append(str(j))
    if a[0]=='empty':
        hap.clear()
