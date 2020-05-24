#Code goes here!
while(1):
    try:
        n=input().strip()
        if len(n)%2!=0:
            x=list(n[:(len(n)//2)])
            y=list(n[(len(n)//2)+1:])
        else:
            x=list(n[:(len(n)//2)])
            y=list(n[(len(n)//2):])
        x.sort()
        y.sort()
        #print(x,y)
        if x==y:
            print("YES")
        else:
            print("NO")
    except:
        break
