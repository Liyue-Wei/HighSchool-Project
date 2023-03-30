#include <iostream>
using namespace std;
int main()
{
    long long i,ans;
    while(cin >> i)
    {
        ans = (i*i*i + 5*i)/6 + 1;
        cout << ans << endl;
        i = 0;
    }
    return 0;
}
