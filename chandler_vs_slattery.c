#include<stdio.h>
int solve(int N)
    { 
        int x,y;
        int a;                              //checks if alice gets the last stone
        int k;                              //iterate
        x=N/4;
        y=N%4;
        if(y==0)                            //check if N in multiple of 4
          return x%4;                       //if N is odd multiple of 4 alice wins
        else                                //if N is not a multiple of 4
        {
          a=0;                          //initialize
          if(x%2)                       //if N is odd multiple of 4
          {
                for(k=1;k<y;++k)        //loop to check if alice gets the last stone
                    a=++k;
                if(a==y)
                    return 1;
                else
                    return 0;
          }
          else                          //if N is even multiple of 4
          {
                for(k=0;k<y;++k)        //loop to check if alice gets the last stone
                    a=++k;
                if(a==y)
                    return 1;
                else
                    return 0;
          }
       }
    }

    int main()
    {
        int T;                              // Test Cases
        int N;                              // No of stones
        int result;
        int i;                              //iterate
        scanf("%d",&T);
        for(i=0;i<T;i++)
        {
            scanf("%d",&N);
            result=solve(N);
            if(result)
               printf("Yes\n");
            else
               printf("No\n");
        }
    return 0;
    }
