def sam(n):
    c=0
    while(True):
        if c>4:
            break
        s=0
        c+=1
        while(n>0):
            r=n%10
            s+=r*r
            n=n//10
        n=s
        #print(n)
        if s==1:
            return 1
    else:
        return 0
t=int(input())
while t:
    t-=1

    if sam(int(input())):
        print("True")
    else:
        print("False")