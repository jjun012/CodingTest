n = int(input())
a,b = map(int,input().split())
dow = int(input())
topping = []
for i in range(n):
    topping.append(int(input()))
topping.sort(reverse=True)
money = a
kalori = dow
won = dow / a

for i in topping:
    money += b
    kalori += i
    now = kalori / money
    if won < now:
        won = now
    else:
        break

print(int(won))
