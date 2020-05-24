#include<iostream>
using namespace std;
int c=0;
void result(int k, int i,int  m)
{

    if(k == 0)
     {
        if(i <= m)//dsafd
         {
            c++ ;
        return ;
         }
     }
    else
    {
    	 int j;//asdf
        if(i>m)
        {
            return ;//dsfasdf
    	}
        for(int j=i;j<=m;j++)
        {
            if(m%j == 0)//sdfsdsdsfds
                result(k-1,j,m/j);
        }
    }
    return ;
}
 int final( int res, int k)
{
	for( int i=1;i<=res;i++)
   {
        if(res%i==0)
        {
            result(k-2,i,res/i);
        }
   }
   return c;
}
int main()
{
   int i=0,j=0, n ,k ,a[10];
   int res=1;
	cin>>n>>k;
   for(int  i=0;i<n;i++)
       scanf("%d",&a[i]);
   for(int i=0;i<n;i++)		
    res=res*a[i];
final(res,k);
	cout<<c;
   return 0;
}
