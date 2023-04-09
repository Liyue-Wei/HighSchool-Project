#include <iostream>
#include <cmath>
using namespace std;
int main(void)
{
    cout << "以降冪排列輸入係數" << endl;
	float a,b,c,d;
	float x1,x2;

    while(cin >> a >> b >> c)
    {
        d=pow(b,2)-(4*a*c);
        cout << "d=" << d << endl;

        x1=(((-1.0*b)+(d))/(2*a));
        x2=(((-1.0*b)-(d))/(2*a));

        if(d < 0)
            cout << "wrong" << '\n';
        else if(d == 0)
            cout << "重根 " << "x=" << x1 << '\n';
        else
            cout << "X1=" << x1 << '\n' << "X2=" << x2 << endl;
    }

    system("pause");
    return 0;
}
