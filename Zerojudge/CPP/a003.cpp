#include <iostream>
using namespace std;
int main()
{
    int m,s,d;
    cin >> m >> d;
    s=(m*2+d)%3;
    if(s==0)    cout << "´¶³q";
    else if(s<2)    cout << "¦N";
    else    cout << "¤j¦N";
    return 0;
}
