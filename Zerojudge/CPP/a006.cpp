#include <iostream>
#include <cmath>
using namespace std;
int main(void)
{
	float a,b,c,d;
	float x1,x2;

    cin >> a >> b >> c;
    d=pow(b,2)-(4*a*c);

    x1=(((-1.0*b)+pow(d,0.5))/(2*a));
    x2=(((-1.0*b)-pow(d,0.5))/(2*a));

    if(d < 0)
        cout << "No real root";
    else if(d == 0)
        cout << "Two same roots x=" << x1;
    else
        cout << "Two different roots x1=" << x1 << " , x2=" << x2;

    return 0;
}

