def function():
    n=int(input())
    a=[int(x) for x in input().split()]
    res=a[0]+a[1]
    x=[res]
    su=[res]
    i=2
    while i<n:
        x.sort()
        #print(x,su)
        if i==n-1:
            sample=a[i]+sample
            i+=1
        elif res>a[i]:
            sample=a[i]+a[i+1]
            x.append(sample)
            i+=2
        else:
            res=x[0]+a[i]
            del x[0]
            x.append(res)
            sample=res
            i+=1
        su.append(sample)
        #print(sample)
    #le=len(x)
    #print(x,su,sum(su))
    le=len(x)
    while len(x)>1:
        x.sort()
        x.append(x[0]+x[1])
        #print(x,x[0],x[1],x[2])
        del x[0]
        del x[0]
        #print(x)
    if le==1:
        print(sum(su))
    else:
        su.append(x[0])
        print(sum(su))
t=int(input())
if t<=10 and t>=1:
    for i in range(t):
        function()
