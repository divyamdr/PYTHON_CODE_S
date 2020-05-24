#include <iostream>
using namespace std;
int main() {
    string  s;
    //read the string
    cin>>s;
    for(int i=0;i<s.length()-1;i++)
    {
        //cout<<s[i]<<endl;
        if(s[i]=='{' &&s[i+1]=='[')
        {
            //checking the module
            cout<<-1<<endl;
            break;
        }
        if(s[i]=='[' &&s[i+1]=='{')
        {
            //return the if exists
            cout<<1<<endl;
            //come out of the loop
            break;
        }
    }
    //return
    return 0;
}

