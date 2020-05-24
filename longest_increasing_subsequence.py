n=int(input())
a=[int(x) for x in input().split()]
lis=[1]*n
p=[]
for i in range(1,n):
    ind=0
    for j in range(i):
        if a[i]>a[j] and lis[i]<lis[j]+1:
            lis[i]+=1
#print(p)
print(max(lis))