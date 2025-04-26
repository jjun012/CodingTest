# 1:1
# 6
# 2:7
# 12
# 3:19
# 24
# 4:37

# 6n+1
n=int(input())
sum=1
cnt=1
while n>sum:
    sum+=6*cnt
    cnt+=1
print(cnt)