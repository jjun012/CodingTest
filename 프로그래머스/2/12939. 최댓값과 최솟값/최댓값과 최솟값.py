def solution(s):
    answer = s.split()
    list1 = list(map(int, answer))
    str_min=min(list1)
    str_max=max(list1)
    
    return ("%s %s"%(str_min,str_max))