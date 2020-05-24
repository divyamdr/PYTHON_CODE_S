#include<bits/stdc++.h>
using namespace std;
int fun(int a[],int n,int k)
{
	int i,j,b[n],sum=0;
	int c[n]={0};
	for(i=0;i<n;i++)
	{
		b[i]=a[i];
		sum+=a[i];
	}
	sort(b,b+n,greater<int>());
	for(i=0;i<n-1;i++)
	{
		for(j=1;j<n-1;j++)
		{
			if(b[i]==a[j])
			{
				if(c[j]<3)
				{
					sum=sum-a[j];
					sum+=k;
					a[j]=-1;
					if(a[j+1]!=-1)
					c[j+1]=c[j]+1;
					else
					c[j+2]=c[j+2]+1;
					
				}
			}
		}
	}
	return sum;
}
int main()
{
	int n,k;
	cin>>n>>k;
	int a[n];
	for(int i=0;i<n;i++)
	cin>>a[i];
	cout<<fun(a,n,k);
}
