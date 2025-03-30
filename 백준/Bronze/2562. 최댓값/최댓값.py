list=[]
for _ in range(9):
    list.append(int(input()))
a=max(list)
print(a)
print(list.index(a)+1)