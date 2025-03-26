import statistics
from collections import Counter
import sys

input=sys.stdin.readline

n=int(input())
list =[int(input())for _ in range(n)]

mean=statistics.mean(list)
list.sort()
median=statistics.median(list)
print(round(mean))
print(median)
def modefinder(list):
    c= Counter(list)
    order=c.most_common()
    cnt=order[0][1]

    modes=[num for num, count in order if count==cnt]

    if len(modes)==1:
        print(modes[0])
        return modes[0]
    else:
        modes.sort()
        print(modes[1])
        return modes[1]
modefinder(list)
print((max(list))-(min(list)))