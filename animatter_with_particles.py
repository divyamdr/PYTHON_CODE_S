import itertools
n=int(input())
a=[int(x) for x in input().split()]
a=list(itertools.combinations(a,2))
res=[]
for i in a:
    a,b=i
    res.append(abs(a-b))
print(min(res))