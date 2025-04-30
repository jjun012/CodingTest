alpha=list(range(97,123))
n=int(input())
for i in range(1,n+1):
    pangram=input().lower()
    check=[0]*26
    for j in pangram:
        if ord(j) in alpha:
            check[ord(j)-97]+=1

    if min(check)==0:
        print(f"Case {i}: Not a pangram")
    elif min(check)==1:
        print(f"Case {i}: Pangram!")
    elif min(check)==2:
        print(f"Case {i}: Double pangram!!")
    elif min(check)==3:
        print(f"Case {i}: Triple pangram!!!")

