n=int(input())
st1=list(input())
st2=list(input())
# durumari
# drmr
chr=['a','e','i','o','u']
if (sorted(st1)==sorted(st2)):
    if st1[0]==st2[0] and st1[-1] == st2[-1]:
        new_st1=[i for i in st1 if i not in chr]
        new_st2=[i for i in st2 if i not in chr]
        if new_st1==new_st2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
    
else:
    print('NO')



