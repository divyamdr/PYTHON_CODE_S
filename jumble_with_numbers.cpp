#include <iostream>
using namespace std;
int main() {
    long long x,y,k,y1;
    long long john,mew,count=0;
    cin>>x>>y>>k;
    y1=y/2;
    if(x<=0||y<=0||k<=0)
    {
    cout<<"Invalid Input"<<endl;
    return 0;
    }
    for(long long i=1;i<=y1;i++)
    {
//outer loop
        if(count>k)
        break;
        mew=i*(( 2*i)-1);//first person
        for(long long j=1;j<=y1;j++)
        {
            // inner loop
         john=j*(j+1)/2; //second person
         if((mew==john)&&(mew>=x&&john<=y))
         {
             count++;
                     //cout<<count<<endl;
             if(count==k)
             {
            cout<<john<<endl;
            return 0;
             }
         }
        }
    }
    if(count<k)
    cout<<"No number is present at this index"<<endl;
    else
    cout<<"Invalid Input"<<endl;
    return 0;
}

