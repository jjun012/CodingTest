n= bin(int(input()))[2:] 
num = 0

for i in range(len(n)):
    if int(n[i]) == 1:
        num += 3 ** (len(n)-i-1)
print(num)