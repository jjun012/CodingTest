m, n = map(int, input().split()) 
universe = [list(map(int, input().split())) for _ in range(m)] 
cnt = 0  

for i in range(m):
    arr_sort = sorted(universe[i]) 
    
    value= {}
    for j in range(n):
        value[arr_sort[j]] = j + 1 
        
    universe[i] = [value[x] for x in universe[i]]

for i in range(m - 1):
    for j in range(i + 1, m):
        if universe[i] == universe[j]:
            cnt += 1

print(cnt)
