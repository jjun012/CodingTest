a,b,c = map(int, input().split())
x,y,z = map(int, input().split())
result = 0

for i in range(3):
    chi = min(a,x)
    result += chi
    a -= chi
    x -= chi

    piz = min(b,y)
    result += piz
    b-= piz
    y -= piz
   
    bur = min(c,z)
    result += bur
    c -= bur
    z -= bur
   
    y,z,x = x // 3, y // 3,z// 3
 
print(result)