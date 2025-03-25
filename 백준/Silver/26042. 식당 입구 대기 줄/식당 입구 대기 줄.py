from collections import deque
import sys

input=sys.stdin.readline

n= int(input())
queue=deque()
cnt=0
back=None

for _ in range(n):
    data=input().split()
    if data[0]=='1':
        stu=int(data[1])
        queue.append(stu)
    else:
        queue.popleft()

    now=len(queue)
    if now>cnt:
        cnt=now
        back=queue[-1]
    elif now==cnt:
        if queue and back is not None and queue[-1]<back:
            back=queue[-1]
print(cnt,back)
