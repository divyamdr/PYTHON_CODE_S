#Code goes here!
n=int(input())
s=[int(x) for x in input().split()]
for i in range(int(input())):
    a=[int(x) for x in input().split()]
    for x in a:
        if x in s:
            c+=1
    if(c==n):
        print("Please Check: "+str(c)+" Abused Words are Found")
    else:
        print("You Have Done Great Job!")