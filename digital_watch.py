def function(n):
    c=0
    if n.count(0)==9:
        print('Impossible')
        return
    for i in range(len(n)):
        if n[i]>9 and n[i]<0:
            c+=1
    if c>=1 or len(n)>9:
        print('Impossible')
        return
    h=''
    s=''
    m=''
    if n.count(0)==6:
        print("Impossible")
        return
    if n.count(0)==4 and n.count(2)==1 and n.count(4):
        print("24:00:00")
        return 
    if n.count(0)==8 and n.count(1)==1:
        print("10:00:00")
        return
    if n.count(2)>=1:
        for i in range(3,-1,-1):
            if i==2 and n.count(2)>=2:
                if n.count(i)>=1:
                    del n[n.index(2)]
                    h='2'+str(i)
                    del n[n.index(i)]
                    break
            if i!=2:
                if n.count(i)>=1:
                    del n[n.index(2)]
                    h='2'+str(i)
                    del n[n.index(i)]
                    break
    elif n.count(1)>=1:
        for i in range(9,-1,-1):
            if i==1 and n.count(2)>=2:
                if n.count(i)>=1:
                    del n[n.index(1)]
                    h='1'+str(i)
                    del n[n.index(i)]
                    break
            if i!=1:
                if n.count(i)>=1:
                    del n[n.index(1)]
                    h="1"+str(i)
                    del n[n.index(i)]
                    break
    elif n.count(0)>=1:
        for i in range(9,-1,-1):
            if i==1 and n.count(2)>=2:
                if n.count(i)>=1:
                    del n[n.index(0)]
                    h='0'+str(i)
                    del n[n.index(i)]
                    break
            if i!=1:
                if n.count(i)>=1:
                    del n[n.index(0)]
                    h='0'+str(i)
                    del n[n.index(i)]
                    break
    else:
        print("Impossible")
        return
    #print(h)
    if h=='':
        print("Impossible")
        return
    for i in range(5,-1,-1):
        if n.count(i)>=1:
            del n[n.index(i)]
            m=str(i)+str(max(n))
            del n[n.index(max(n))]
            break
    #print(m)
    if m=='':
        print("Impossible")
        return
    for i in range(5,-1,-1):
        if n.count(i)>=1:
            del n[n.index(i)]
            s=str(i)+str(max(n))
            del n[n.index(max(n))]
            break
    #print(s)
    if s=='' or h=='':
        print("Impossible")
        return
    print(str(h)+':'+str(m)+':'+str(s))
    
n=[int(x) for x in input().split(',')]
function(n)
