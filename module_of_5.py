import time
start_time = time.time()
def divide(n):
    s=0
    while(n>0):
        s+=n%10
        n=n//10
    if s%5==0:
        return 1
    else:
        return 0
t=int(input())
while t:
    t-=1
    n,k=input().split()
    n=int(n)
    k=int(k)
    i=0
    x=((n//5)+k)*5
    while True:
        if i==1:
            print(x-1)
            break
        i=divide(x)
        x+=1
print("--- %s seconds ---" % (time.time() - start_time))
    