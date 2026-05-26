def solution(name, yearning, photo):
    answer = []
    num=dict(zip(name,yearning))
    for i in photo:
        result=0
        for j in i:
            if j in num:
                result+=num[j]
        answer.append(result)
    return answer