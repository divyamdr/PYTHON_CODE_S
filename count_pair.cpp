#include<iostream>
#include<unordered_map>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int a[4];
	a[0]=1;
	a[1]=5;
	a[2]=7;
	a[3]=-1;
	int sum=6;
	
	unordered_map<int,int> m;
	for(int i=0;i<4;i++)
	m[a[i]]++;
	for(int i=0;i<4;i++)
	cout<<m[i]<<endl;
	int twice_count=0;
	for(int i=0;i<4;i++)
	{
		twice_count +=m[sum-a[i]];
		if(sum-a[i]==a[i])
		twice_count--;	
	}
	cout<<twice_count/2;
	
	return 0;
}
