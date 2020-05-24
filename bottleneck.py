n=int(input())
a=[int(x) for x in input().split()]
result=0
a.sort()
for i in range(n-1):
    for j in range(n):
        if a[i]<a[j]:
            a[i]=0
for i in range(n):
    if a[i]>0:
        result+=1
if result>0:
    print(result)
else:
    print(n)