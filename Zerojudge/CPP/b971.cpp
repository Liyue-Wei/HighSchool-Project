#include<iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    int a1,an,d;
    while(cin >> a1 >> an >> d){
        int s=(an-a1)/d;
        for(int i=0; i<=s; i++) cout << a1+i*d << " ";
        cout << endl;
    }
    return 0;
}
