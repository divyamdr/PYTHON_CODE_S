def function(n,a):
    a.sort()
    x=0
    while(len(a)>1):
        a.append(a[0]+a[1])
        x+=a[0]+a[1]
        del a[0]
        del a[0]
        #print(a)
        a.sort()
    print(x)
t=int(input())
if t<=10 and t>=1:
    for i in range(t):
        n=int(input())
        a=[int(x) for x in input().split()]
        function(n,a)