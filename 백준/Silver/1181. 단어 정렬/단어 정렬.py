n=int(input())
st=[]
for i in range(n):
    s=input()
    st.append(s)
st=set(st)
st=list(st)
new_st=sorted(st,key=lambda x : (len(x),x))
for i in range(len(new_st)):
    print(new_st[i])
    i+=1