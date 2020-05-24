t=int(input())
while t:
    t-=1
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    i=c
    flag=0
    while(i>=b and b<a):
        k=i%a
        #print(k)
        if k==b:
            k=i%1000000000
            print(k)
            flag=1
            break
        else:
            i-=1
    if flag==0:
        print(-1)