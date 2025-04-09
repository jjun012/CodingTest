num = list(input())

i=0
j=0
while j<len(num):
    i+=1
    for n in str(i):
        if j < len(num) and n==num[j]:
            j+=1
    
print(i)

