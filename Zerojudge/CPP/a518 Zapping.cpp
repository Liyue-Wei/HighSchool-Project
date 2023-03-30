#include <iostream>
using namespace std;
int main()
{
    int i,n,t;
    while(cin >> i >> n)
    {
        if(i-n>0)
        {
            t=n;
            n=i;
            i=t;
            if(n-i>50)
                cout << (100-n)+i << endl;
            else
                cout << n-i << endl;
        }

        else if(i==(-1) && n==(-1))
            return 0;

        else if(i==n)
        {
            cout << "0" << endl;
        }

        else
        {
            if(n-i>50)
                cout << (100-n)+i << endl;
            else
                cout << n-i << endl;
        }
    }
    return 0;
}
