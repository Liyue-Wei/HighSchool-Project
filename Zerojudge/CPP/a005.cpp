#include <iostream>
using namespace std;
int a,b,c,d,q1,q2,q3,q4;
bool ans;
int main(void)
{
    int i;
    cin >> i;
    for(i;i>0;i--)
    {
        cin >> a >> b >> c >> d;
        q1=b-a; q2=d-c; q3=b/a; q4=d/c;

        if(q1==q2)
            ans=true;

        else if(q3==q4)
            ans=false;

        if(ans==true)
            cout << a << " " << b << " " << c << " " << d << " " << d+q1 << endl;
        else if(ans==false)
            cout << a << " " << b << " " << c << " " << d << " " << d*q3 << endl;
    }
    return 0;
}

