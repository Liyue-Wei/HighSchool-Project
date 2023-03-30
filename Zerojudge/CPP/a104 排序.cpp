#include <iostream>
using namespace std;
int main(void)
{
    int i,n;
    while(cin >> i && i>0)
    {
    int cha[i];
    for(n=0;n<i;n++)
    {
        cin >> cha[n];
    }

    for(int t=i-1;t>0;t--)
    {
        while(cha[t-1]<cha[t])
        {
            int r=cha[t-1];
            cha[t-1]=cha[t];
            cha[t]=r;
            t=i-1;
        }
    }
    //for(n=0;n<i;n++) cout << cha[n] << " "; cout << endl;
    for(int test=i-1;test>=0;test--)
    {
        cout << cha[test] << " ";
        //cout << endl;
    }
    cout << endl;
    }
}
