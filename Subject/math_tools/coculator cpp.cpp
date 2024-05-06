#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
    {
        cout << "choose your formula" << endl << "1 == pow , 2 == sqrt , 3 == plus , 4 == minus , 5 == multiply" << endl << "6 == divide , 7 == double plus , 8 == gcd , 9 == 一元二次方程式" << endl ;
        int i;
        while(cin >> i)

    if(i==1 || i==2 || i==3 || i==4 || i==5 || i==6 || i==7 || i==8 || i==8 || i==9 || i==0)
    {
        cout << "continue" << endl ;

        if(i==1)
        {
            cout << "pow" << endl ;
            double a,b,c ;
            cin >> a >> b ;
            c=pow(a,b);

            cout << setprecision(128)<< "c= " << c << endl << "ctrl z for pause" << endl << "keep typing for continue" << endl ;

        }

        else if(i==2)
        {
            cout << "sqrt" << endl ;
            double a,b,c ;
            cin >> a >> b ;
            c=pow(a,1/b);

            cout << setprecision(128) << "c= " << c << endl << "ctrl z for pause" << endl << "keep typing for continue" << endl ;
        }

        else if(i==3)
        {
            cout << "plus" << endl ;
            double a,b,c ;
            cin >> a >> b ;
            c=a+b;

            cout << setprecision(128) << "c= " << c << endl << "ctrl z for pause" << endl << "keep typing for continue" << endl ;
        }

        else if(i==4)
        {
            cout << "minus" << endl ;
            double a,b,c ;
            cin >> a >> b ;
            c=a-b;

            cout << setprecision(128) << "c= " << c << endl << "ctrl z for pause" << endl << "keep typing for continue" << endl ;
        }

        else if(i==5)
        {
            cout << "multiply" << endl ;
            double a,b,c ;
            cin >> a >> b ;
            c=a*b;

            cout << setprecision(128) << "c= " << c << endl << "ctrl z for pause" << endl << "keep typing for continue" << endl ;
        }

        else if(i==6)
        {
            cout << "divide" << endl ;
            double a,b,c ;
            cin >> a >> b ;
            c=a/b;

            cout << setprecision(128) << "c= " << c << endl << "ctrl z for pause" << endl << "keep typing for continue" << endl ;
        }

        else if(i==7)
        {
            int b,c;
            int a=1;
            int sum=0;
            cout << "double plus " << endl << "single or double" << endl;
            cin >> b >> c;
            if(c==1 || c==2)
                {
                    while(a<=b)
                    {
                    sum+=a;
                    a+=c;
                    }
                    cout << "ans= " << sum << endl;

                }
            else
                {
                    cout << "wrong number" << '\a' << endl << "ctrl z for pause" << endl << "keep typing for continue" << endl ;
                }
        }

        else if(i==8)
        {
            int a,b;
            cout << "gcd" << endl;
            cin >> a >> b;
            while(a%b!=0)
            {
                int r=a%b;
                a=b;
                b=r;
            }
            cout << "gcd= " << b << endl << "ctrl z for pause" << endl << "keep typing for continue" << endl ;
        }

        else if(i==9)
        {
            cout << "以降冪排列輸入係數" << endl << "輸入一個係數一次Enter" << endl;
            long long a,b,c;
            int d;

            cin >> a >> b >> c;
            d=pow(b,2)-(4*a*c);
            cout << "d=" << d << endl;

            if(d < 0)
                cout << "wrong";
            else if(d == 0)
                cout << "重根 " << "x=" << (((-b)+pow(d,(0.5)))/(2*a)) << endl;
            else
                cout << "正根=" << (((-b)+pow(d,(0.5)))/(2*a)) << " " << "負根=" << (((-b)-pow(d,(0.5)))/(2*a)) << endl;

			cout << "ctrl z for pause" << endl << "keep typing for continue" << endl ;
        }

        else if(i==0)
        {

        }
    }

        else
        {
            cout << "wrong number" << endl << '\a' << "ctrl z for pause" << endl << "keep typing for continue" << endl ;
        }
system("pause");
return 0;
    }
