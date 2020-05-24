def su(n):
    s=0
    while(n>0):
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
if su(n)<9:
    print(su(n))
else:
    s=su(n)
    while(s>9):
        s=su(s)
    print(s)