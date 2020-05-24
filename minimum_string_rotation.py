n=int(input())
x=[]
for i in range(n):
    x.append(input())
print(x)
mi,co=9999,0
for i in range(n):
    y=x[i]
    #print(y)
    co=0
    for j in range(1,len(y)):
        co+=x.count(y)
        y=y[1:]+y[0]
    if mi>co:
        mi=co
print(mi)