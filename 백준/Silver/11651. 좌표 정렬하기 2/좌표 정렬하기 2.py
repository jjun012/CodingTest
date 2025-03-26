import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([y, x])

result = sorted(arr)

for y, x in result:
    print(x, y)