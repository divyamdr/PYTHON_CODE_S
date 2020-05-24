n=input()
k=list(str(n))
sum=0
for i in range(0,len(k),2):
    sum+=int(k[i])
if sum%2==0:
    print(n)
else:
    print('not')