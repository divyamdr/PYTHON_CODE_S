#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int divide(int n)
{
	int sum=0,c;
	while(n)
	{
		c=n%10;
		n=n/10;
		sum+=c;
	}
	if(sum%5==0)return 1;
	return 0;
}
int main()
{
int a,b;
cin>>a>>b;
int k=(a/5+b)*5;
int i=0;
while(!i)
{
	i=divide(k);
	k++;
}
cout<<k-1;
}
