#Code goes here!
for i in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    m=a[0]
    k=0
    r=a.count(0)
    if r!=0:
        for i in range(n):
            if a[i]==0:
                k+=1
                continue
            if a[i]>m:
                k+=2
                m=a[i]
        print(k)
    else:
        print(0)
    while i<n:
        if a[i]==0:
            del a[i]
            n-=1
        else:
            i+=1