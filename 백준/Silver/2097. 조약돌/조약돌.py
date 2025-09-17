import sys

a = int(sys.stdin.readline().strip())

if a == 0:
    print(0)
elif a == 1:
    print(4)
else:
    i = 0
    while i * i < a:
        i += 1
    num = i

    if (num - 1) * num > a:
        cir = (num - 2 + num - 1) * 2
    else:
        cir = (num - 1) * 4

    print(cir)