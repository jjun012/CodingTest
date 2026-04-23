def solution(x):
    
    num_list=list(map(int,str(x)))
    answer = sum(num_list)
    if x%answer==0:
        return True
    else:
        return False