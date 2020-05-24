def sol(x,y,k):
    count=0
    y1=y//2+1
    if(x<=0 or y<=0):
        print("Invalid Input")
        return 0
    for i in range(1,y1+1):
#//outer loop
        if(count>k):
            break
        mew=i*(( 2*i)-1)#//first person
        for j in range(1,y1+1):
            #// inner loop
            john=j*(j+1)/2 #//second person
            if((mew==john)and (mew>=x and john<=y)):
         #{
                count+=1
                     #//cout<<count<<endl;
                if(count==k):
                    print(john)
            ##}
         #}
        #}
    #}
    if(count<k):
        print("No number is present at this index")
    else:
        print("Invalid Input")

x,y,z=map(int,input().split())
sol(x,y,z)
