#Code goes here!
n=int(input())
a=[int(x) for x in input().split()]
lis=[]
i=0
k=0
l=[a[0]]
while(i<n):
    if k==n:
        break
    k+=1
    lis.append(l)
    l=[]
    for j in range(i,n):

        if j==n-1:
            #print(j)
            if a[j-1]<=a[j]:
                l.append(a[j])
                break
            else:
                break
        if a[j]<=a[j+1]:
            l.append(a[j])
            continue
        else:
            l.append(a[j])
            break
    i=j+1
    #print(i,j)
lis.append(l)
#print(lis,l)
res=lis[0]
for i in range(len(lis)-1):
    if len(lis[i])<len(lis[i+1]):
        res=lis[i+1]
print(*res)