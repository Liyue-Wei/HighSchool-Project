#include <iostream>
using namespace std;
long a1,a2,a3,b1,b2,b3;
int i=12000;
long ar1[12000],ar2[12000],ar3[12000];
int main()
{
    while(cin >> a1 >> b1 >> a2 >> b2 >> a3 >> b3)
    {
        for(int n=0;n<i;n++)
        {
            if(n==0)
            {
                ar1[0]=a1;
                ar2[0]=a2;
                ar3[0]=a3;
            }
            else
            {
                ar1[n]=(ar1[n-1]*a1)+b1;
                ar2[n]=(ar2[n-1]*a2)+b2;
                ar3[n]=(ar3[n-1]*a3)+b3;
            }
        }
        for(int n=0;n<i;n++)
        {

        }
    }
    return 0;
}
/*
#include
using namespace std;
int main()
{
int a,b,c,n;
while(cin>>a>>b>>c)
{
n=(a*70+b*21+c*15)%105
if(n>100||n else cout<<n<<endl;
}
return 0;
}
*/
