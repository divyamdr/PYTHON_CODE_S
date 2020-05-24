t=int(input())
while t>0:
    t-=1
    c=0
    n,x=map(int,input().split())
    for i in range(n):
        a,b=map(int,input().split())
        if(a>=x and b>=x):
            c+=1
    print(c)