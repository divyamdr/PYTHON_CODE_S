def pattern(n,x,space):
    k=space
    for i in range(n):
        for j in range(k):
            print(end=' ')
        k = k - 1
        for j in range(0,x):
            print("*", end="")
        print("\r")
        x+=2
def function(n):
    if n==1:
        print("*")
        return 0
    if n==2:
        print("*")
        print("*")
        return 0
    space=2*n+1
    pattern(n+1,1,space//2)
    for i in range(n-2,0,-1):
        pattern(i+1,3,space//2-1)
    for i in range(2):
        for j in range(space//2):
            print(end=' ')
        print("*")
n=int(input())
function(n)