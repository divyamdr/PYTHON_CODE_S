n=int(input())
a='11'
if n==1:
    print(1)
else:
    i=0
    count=1
    res=[]
    ind=2
    while(ind<n):
        res=''
        for i in range(len(a)-1):
            if i==len(a)-2:
                if a[i]==a[i+1]:
                    res=res+str(count+1)
                    res=res+str(a[i])
                    break
                if a[i]!=a[i+1]:
                    res=res+str(count)
                    res=res+str(a[i])
                    res=res+str(1)
                    res=res+str(a[i+1])
                    break
            if a[i]==a[i+1]:
                count+=1
                i+=1
                continue
            if a[i]!=a[i+1]:
                res=res+str(count)
                res=res+str(a[i])
                #print(res)
                count=1
        a=res
        ind+=1
    print(a)