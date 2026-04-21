def solution(n, control):
    new_list=list(control)
    for i in new_list:
        if i=='w':
            n+=1
        elif i=='s':
            n-=1
        elif i=='d':
            n+=10
        else:
            n-=10
    return n