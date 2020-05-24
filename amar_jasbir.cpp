#include <iostream>
using namespace std;
int main() {
    long long n;
    cin>>n;
    long long a[n];//creating as=n array
    int finall=0;//intialize as 0
    for(long long i=0;i<n;i++)
    {
        //reading
    cin>>a[i];
    //reading the elements in the list
    finall=finall^a[i];
    //storing the result in the finall as xor operation
    }
    // we having the two winners the game
    //one is jasbir and other is aman
    if(finall!=0)
    cout<<"Aman"<<endl;
    //execute the if statement and return the aman as the winner
    else
    cout<<"Jasbir"<<endl;
    //return jasbir as the winner
//final result
    return 0;
    pause(1);
}

