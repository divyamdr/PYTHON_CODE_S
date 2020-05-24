#Code goes here!
for i in range(int(input())):
    a=list(input().strip())
    b=list(input().strip())
    x=0
    while x<len(a):
        if a[x]=='#' and x>0:
            del a[x-1]
            del a[x-1]
            x-=1
        elif a[x]=='#' and x==0:
            del a[x]
        else:
            x+=1
        #print(a,x)
    i=0
    while i<len(b):
        if b[i]=='#' and i>0:
            del b[i-1]
            del b[i-1]
            i-=1
        elif b[i]=='#':
            del b[i]
        else:
            i+=1
    a=''.join(a)
    b=''.join(b)
    #print(a,b)
    if len(a)==len(b):
        print("True")
    else:
        print("False")