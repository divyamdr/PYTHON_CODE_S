import itertools
n,p=map(int,input().split(","))
a=[int(x) for x in input().split(",")]
a=list(itertools.combinations(a,3))
count=0
for i in a:
    x=sum(i)
    if x%p==0:
        count+=1
print(count%1009)