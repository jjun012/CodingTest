n = int(input())
num = list(map(int, input().split()))
cnt = 0 

for i in num:
    if i < 2:  
        continue

    is_prime = True 

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break 

    if is_prime: 
        cnt += 1

print(cnt) 
