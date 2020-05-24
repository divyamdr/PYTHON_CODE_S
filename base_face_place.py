#Code goes here!
n=int(input())
face=input().strip()
place=int(input())
base=2
result=[]
for base in range(2,37):
    s=''
    next=n
    while(next>0):
        r=next%base
        if r>9:
            s+=(chr(65+r-10))
        else:
            s+=str(r)
        next=next//base
    if place<=len(s)-1:
        if s[place]==str(face):
            result.append(base)
print(*result,sep=' ')