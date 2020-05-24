def factor(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=result(k-2,i,m/i)
    return c
def result(k,i,m):
    if(k==0):
        if ( i <= m):
            c+=1
        return c
    else:
        if(i>m):
            return c
        for j in range(i,m+1,1):
            if(m%j == 0):
                c=result(k-1,j,m/j)
    
n,k=map(int,input().split())
a=[int(x) for x in input().split()]
res=1
for i in range(n):
    res=res*a[i]
c=factor(res)
print(c)
}