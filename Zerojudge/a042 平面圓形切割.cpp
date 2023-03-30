#include <iostream>
using namespace std;
int main()
{
    int n,t;
    while(cin >> n)
    {
        int sum = 2;
        for (t=1;t<=n;t++)
        {
            sum += (n-t)*2;
        }
        cout << sum << '\n';
    }
    return 0;
}
