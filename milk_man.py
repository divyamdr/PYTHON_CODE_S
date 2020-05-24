import itertools
no=[1,5,7,10]
x=list(itertools.permutations(no,4))
n=int(input())
l=[]
for i in x:
    s=0
    k=n
    a,b,c,d=i
    s+=k//a
    k=k%a
    s+=k//b
    k=k%b
    s+=k//c
    k=k%c
    s+=k//d
    k=k%d
    l.append(s)
    #print(a,b,c,d)
print(min(l))