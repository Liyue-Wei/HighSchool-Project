#include <iostream>
using namespace std;
int main()
{
    int i;
    while(cin >> i)
    {
        if(i%4==0 && i%100!=0 || i%400==0)  cout << "�|�~" << endl;
        else    cout << "���~" << endl;
    }
    return 0;
}

