#Code goes here!
for i in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    i=0
    r=0
    while i<n:
        if a[i]==0:
            del a[i]
            r+=1
            n-=1
        else:
            i+=1
    k=1
    m=0
    #print(a)
    if len(a)==0:
        print(r)
    elif r==0:
        print(0)
    else:
        for i in range(n):
            flag=0
            k=1
            for j in range(i,n-1):
                #print(a[j+1],a[j])
                if a[j]<a[j+1] and flag==0:
                    #print(a[j],a[j+1])
                    k+=1
                    m=max(k,m)
                else:
                    break
        print(m+r)