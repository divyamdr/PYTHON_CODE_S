#Code goes here!
n=int(input())
x=[]
k=0
r1=0
for i in range(n):
    a=[int(x) for x in input().split()]
    x.append(a)
    new=list(set(a))
    if(len(new)!=n):
        r1+=1
    k+=x[i][i]
row=[]
col=[]
c=0
for i in range(n):
    r=[]
    for j in range(n):
        r.append(x[j][i])
    new=list(set(r))
    if len(new)!=n:
        c+=1
print(k,r1,c)