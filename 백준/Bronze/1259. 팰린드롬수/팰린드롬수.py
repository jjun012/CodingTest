while True:
    num=list(map(int,input()))
    re_num=list(reversed(num))
    if sum(num)==0:
        break
    if num==re_num:
        print('yes')
    else:
        print('no')
