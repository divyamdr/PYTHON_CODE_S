#Code goes here!
#Code goes here!
def count(n):
    s=0
    while(n>0):
        s+=n%10
        n=n//10
    return s
for i in range(int(input())):
    n=int(input())
    st=''
    k=[0]*n
    for i in range(n):
        d,l=map(int,input().split())
        print(d,l)
        k[l-1]=d
    for i in range(n):
        s+=str(k[i])
    s=int(s)
    q=0
    for i in range(1,s+1):
        if(1<=s and s<=9):
            q+=n
        else:
            q+=count(n)
    x=count(q)
    print(str(q)+"=>"+str(x))
