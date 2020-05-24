import itertools
n=[str(x) for x in input().split()]
k=int(input())
n=list(itertools.combinations(n,2))
l=[]
for i in n:
    x=[]
    a,b=i
    if (int(a)+int(b))%k==0:
        x.append(a)
        x.append(b)
        l.append(x)

print(l)
print(len(l))