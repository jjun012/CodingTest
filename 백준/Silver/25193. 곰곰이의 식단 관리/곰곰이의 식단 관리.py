import math
s=int(input())
food=input()
a=0
b=0
for i in food:
    if 'C' in i:
        a+=1
    else:
        b+=1
print(math.ceil(a/(b+1)))