import itertools
import math
def prime(n):
    if n==1 or n==0:
        return False
    if n==2 or n==3 or n==5:
        return True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
l=int(input())
n=list(itertools.permutations(range(l+1), 2))
x=[]
res=[]
for i in n:
    a,b=i
    x2=str(a)+str(b)
    x1=str(b)+str(a)
    if prime(a+b) and not(x1 in x or x2 in x):
        x.append(str(a)+str(b))
for i in range(1,l+1):
    if prime(2*i):
        x.append(str(i)*2)
print(len(x))
